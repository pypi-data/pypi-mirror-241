""" Ground motion model by Campbell and Bozorgnia (2019) for Ia and CAV . 
"""

import numpy as np
cimport numpy as np
cimport cython
import CampbellBozorgnia2014
from libc.math cimport pi, cos, pow, sqrt, exp, fmax, log

__author__ = 'A. Renmin Pretell Ductram'

#===================================================================================================
# Ia (0)/CAV (1): phi
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
cdef get_phi_cy(int IM,double M,double Vs30,double A_1100):
    
    cdef double k_1, k_2, c, n, phi_lnAF, phi_1, phi_2, rho_1, rho_2
    cdef double phi_lnY, rho_lnPGA_lnY, alpha, phi_lnPGA_B, phi
    
    if IM == 1:
        k_1      =  400.
        k_2      = -1.311
        c        =  1.88
        n        =  1.18
        phi_lnAF =  0.3 
        phi_1    =  0.514
        phi_2    =  0.394
        rho_1    =  0.842
        rho_2    =  0.78
    elif IM == 0:
        k_1      =  400.
        k_2      = -1.982
        c        =  1.88
        n        =  1.18
        phi_lnAF =  0.616
        phi_1    =  1.174
        phi_2    =  0.809
        rho_1    =  0.948
        rho_2    =  0.911

    if M <= 4.5:
        phi_lnY       = phi_1*1
        rho_lnPGA_lnY = rho_1*1
    elif M <= 5.5:
        phi_lnY = phi_2+(phi_1-phi_2)*(5.5-M)
        rho_lnPGA_lnY = rho_2+(rho_1-rho_2)*(5.5-M)
    else:
        phi_lnY       = phi_2*1
        rho_lnPGA_lnY = rho_2*1
    phi_lnY_B = sqrt(pow(phi_lnY,2)-pow(phi_lnAF,2))

    alpha = 0
    if Vs30 < k_1:
        alpha = k_2*A_1100*(pow(A_1100+c*pow(Vs30/k_1,n),-1)-pow(A_1100+c,-1))
    
    phi_lnPGA_B = CampbellBozorgnia2014.get_phi_cy(M)

    return sqrt(pow(phi_lnY_B,2)+pow(phi_lnAF,2)+pow(alpha,2)*pow(phi_lnPGA_B,2)+2*alpha*rho_lnPGA_lnY*phi_lnY_B*phi_lnPGA_B)

#===================================================================================================
# Ia (0)/CAV (1): phi
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
cdef get_tau_cy(int IM,double M,double Vs30,double A_1100):

    cdef double k_1, k_2, c, n, phi_lnAF, phi_1, phi_2, rho_1, rho_2
    cdef double tau_lnY, rho_lnPGA_lnY, alpha, tau_lnPGA_B, tau

    if IM == 1:
        k_1   =  400.
        k_2   = -1.311
        c     =  1.88
        n     =  1.18
        tau_1 =  0.276
        tau_2 =  0.257
        rho_1 =  0.842
        rho_2 =  0.78
    elif IM == 0:
        k_1   =  400.
        k_2   = -1.982
        c     =  1.88
        n     =  1.18
        tau_1 =  0.614
        tau_2 =  0.435
        rho_1 =  0.948
        rho_2 =  0.911

    if M <= 4.5:
        tau_lnY       = tau_1*1
        rho_lnPGA_lnY = rho_1*1
    elif M <= 5.5:
        tau_lnY       = tau_2+(tau_1-tau_2)*(5.5-M)
        rho_lnPGA_lnY = rho_2+(rho_1-rho_2)*(5.5-M)
    else:
        tau_lnY       = tau_2*1
        rho_lnPGA_lnY = rho_2*1
    tau_lnY_B = tau_lnY*1

    alpha = 0
    if Vs30 < k_1:
        alpha = k_2*A_1100*(pow(A_1100+c*pow(Vs30/k_1,n),-1)-pow(A_1100+c,-1))

    tau_lnPGA_B = CampbellBozorgnia2014.get_tau_cy(M)
        
    return sqrt(pow(tau_lnY_B,2)+pow(alpha,2)*pow(tau_lnPGA_B,2)+2*alpha*rho_lnPGA_lnY*tau_lnY_B*tau_lnPGA_B)

#===================================================================================================
# Ia (0)/CAV (1): mu, phi, tau
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
def CampbellBozorgnia2019_cy(int IM,double M,double fwidth,double fdip,double Z_tor, double Z_hyp,
                             double[:] R_JB,double[:] R_rup,double[:] R_x,double[:] Vs30,double[:] Z2p5,
                             int fnm,int frv,region):
	
    """
    Parameter
    =========
    IM: 0 for Ia, and 1 for CAV.
    M: Earthquake magnitude.
    fwidth: Fault width in km.
    fdip: Fault dip in deg.
    Z_hyp: Hypocentral depth in km.
    Z_tor: Depth to top of fault rupture in km.
    R_JB: Joyner-Boore distance in km.
    R_rup: Rupture distance in km.
    R_x: Rx distance in km.
    Vs30: Site Vs30. 
    Z2p5: Depth to Vs = 2.5 km/s.
    fnm: 1 for normal/normal-oblique fault, 0 otherwise.
    frv: 1 for reverse/reverse-oblique fault, 0 otherwise.
    region: Earthquake country.

    Returns
    =======
    mean, phi, tau for the selected IM.
    """

    cdef int N_sites = len(R_JB)
    cdef double Vs30_R = 1100.
    cdef double Z2p5_R = exp(7.089-1.144*log(1100.))
    cdef double[:] mu_im  = np.zeros(N_sites, dtype='float64')
    cdef double[:] phi_im = np.zeros(N_sites, dtype='float64')
    cdef double[:] tau_im = np.zeros(N_sites, dtype='float64')
    cdef double mu_pga
    cdef int i
    
    for i in range(N_sites):
        mu_pga = CampbellBozorgnia2014.get_mu_cy(2,M,fwidth,fdip,Z_tor,Z_hyp,R_JB[i],R_rup[i],R_x[i],Vs30_R,Z2p5_R,0.,fnm,frv,region)
        mu_im[i]  = CampbellBozorgnia2014.get_mu_cy(IM,M,fwidth,fdip,Z_tor,Z_hyp,R_JB[i],R_rup[i],R_x[i],Vs30[i],Z2p5[i],exp(mu_pga),fnm,frv,region)
        phi_im[i] = get_phi_cy(IM,M,Vs30[i],exp(mu_pga))
        tau_im[i] = get_tau_cy(IM,M,Vs30[i],exp(mu_pga))

    return np.asarray(mu_im),np.asarray(phi_im),np.asarray(tau_im)
