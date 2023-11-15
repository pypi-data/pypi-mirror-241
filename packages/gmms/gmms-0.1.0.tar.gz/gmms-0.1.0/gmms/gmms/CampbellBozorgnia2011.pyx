""" Ground motion model by Campbell and Bozorgnia (2011) for CAVdp. 
"""

import numpy as np
cimport numpy as np
cimport cython
import CampbellBozorgnia2010
from libc.math cimport pow, sqrt, log, exp, fmin, fmax

__author__ = 'A. Renmin Pretell Ductram'

#===================================================================================================
# CAVdp: mu
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
cdef get_mu_cy(int PSVcheck,double M,double fdip,double fZtor,double R_JB,double R_rup,double R_x,double Vs30,double Z1p0,double Z2p5,int fnm,int frv):
    
    cdef double lnCAVgm, mu
    cdef double c_0, c_1, c_2, c_3

    if PSVcheck == 1:
        c_0 =  0.0072
        c_1 =  1.115
        c_2 = -0.067
        c_3 = -0.00330
    else:
        c_0 =  0.0152
        c_1 =  1.105
        c_2 = -0.044
        c_3 = -0.00369
    
    lnCAVgm = CampbellBozorgnia2010.get_mu_cy(1,M,fdip,fZtor,R_JB,R_rup,R_x,Vs30,Z2p5,fnm,frv)
    return c_0+c_1*lnCAVgm+c_2*(M-6.5)*(M>=6.5)+c_3*R_rup

#===================================================================================================
# CAVdp: phi
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
cdef get_phi_cy(int CAVgmType,int PSVcheck,double alpha):

    cdef double c_1 
    cdef double phi_lnCAVdp, phi_lnAF_PGA, phi_lnPGA, phi_lnAF_CAVgm, phi_lnCAVgm, rho_lnCAVgm, phi
    
    if CAVgmType == 0:
        if PSVcheck == 1:
            return 0.147
        else:
            return 0.131
    
    elif CAVgmType == 1:
        if PSVcheck == 1:
            phi_lnCAVdp = 0.439
        else:
            phi_lnCAVdp = 0.430
            
        c_1            = 0 
        phi_lnAF_PGA   = 0.3000
        phi_lnPGA      = 0.478
        phi_lnAF_CAVgm = 0.300
        phi_lnCAVgm    = 0.371
        rho_lnCAVgm    = 0.735
        
        phi_lnPGA_B   = sqrt(pow(phi_lnPGA,2)-pow(phi_lnAF_PGA,2))
        phi_lnCAVgm_B = sqrt(pow(phi_lnCAVgm,2)-pow(phi_lnAF_CAVgm,2))
        
        phi_1 = pow(phi_lnCAVgm_B,2)
        phi_2 = pow(phi_lnAF_CAVgm,2)
        phi_3 = pow(alpha,2)*pow(phi_lnPGA_B,2)
        phi_4 = 2*alpha*rho_lnCAVgm*phi_lnCAVgm_B*phi_lnPGA_B
        
        return sqrt(pow(phi_lnCAVdp,2)+(pow(c_1,2))*(phi_1+phi_2+phi_3+phi_4))

#===================================================================================================
# CAVdp: tau
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
cdef get_tau_cy(int CAVgmType,int PSVcheck):
    
    cdef double c_1
    cdef tau_lnCAVdp, tau_lnCAVgm, tau

    if CAVgmType == 0:
        return 0.115
    
    elif CAVgmType == 1:

        if PSVcheck == 1:
            tau_lnCAVdp = 0.247
        else:
            tau_lnCAVdp = 0.245
        
        c_1         = 0 
        tau_lnCAVgm = 0.196

        return sqrt(pow(tau_lnCAVdp,2)+(pow(c_1,2))*(pow(tau_lnCAVgm,2)))

#===================================================================================================
# CAVdp: mu, phi, tau
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
def CampbellBozorgnia2011_cy(double M,double fdip,double fZtor,
                             double[:] R_JB,double[:] R_rup,double[:] R_x,double[:] Vs30,double[:] Z1p0,double[:] Z2p5,
                             int fnm,int frv,int CAVgmType,int PSVcheck):

    """
    Parameter
    =========
    M: Earthquake magnitude.
    fdip: Fault dip in deg.
    fZtor: Depth to top of fault rupture in km.
    R_JB: Joyner-Boore distance in km.
    R_rup: Rupture distance in km.
    R_x: Rx distance in km.
    Vs30: Site Vs30. 
    Z1p0: Depth to Vs = 1 km/s.
    Z2p5: Depth to Vs = 2.5 km/s.
    fnm: '1' for normal/normal-oblique fault, '0' otherwise.
    frv: '1' for reverse/reverse-oblique fault, '0' otherwise.
    CAVgm_type: 0 for recorded, and 1 for gmm-based.
    PSV_check: 0 for no check, and 1 for yes.

    Returns
    =======
    CAVdp mean, phi, tau.
    """
    
    cdef int N_sites = len(R_JB)
    cdef double[:] A_1100 = np.zeros(N_sites, dtype='float64')
    cdef double[:] alpha = np.zeros(N_sites, dtype='float64')
    cdef double[:] mu_im = np.zeros(N_sites, dtype='float64')
    cdef double[:] phi_im = np.zeros(N_sites, dtype='float64')
    cdef double[:] tau_im = np.zeros(N_sites, dtype='float64')
    cdef int i

    for i in range(N_sites):
        A_1100[i] = CampbellBozorgnia2010.get_mu_cy(0,M,fdip,fZtor,R_JB[i],R_rup[i],R_x[i],1100.,Z2p5[i],fnm,frv)
        A_1100[i] = exp(A_1100[i])
        alpha[i]  = CampbellBozorgnia2010.get_alpha_cy(Vs30[i],A_1100[i])
        
        mu_im[i]  = get_mu_cy(PSVcheck,M,fdip,fZtor,R_JB[i],R_rup[i],R_x[i],Vs30[i],Z1p0[i],Z2p5[i],fnm,frv)
        phi_im[i] = get_phi_cy(CAVgmType,PSVcheck,alpha[i])
        tau_im[i] = get_tau_cy(CAVgmType,PSVcheck)

    return np.asarray(mu_im),np.asarray(phi_im),np.asarray(tau_im)
