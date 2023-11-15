""" A suite of functions to compute distances for ground motion model calculations.
"""

import numpy as np
cimport numpy as np
import nvector as nv
cimport cython
from libc.math cimport pi, sin, cos, tan, atan, atan2, pow, sqrt, isinf

__author__ = 'A. Renmin Pretell Ductram'

#===================================================================================================
# Get min from an array of numbers
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
def argmin_cy(double[:] array_A):

	cdef int N = len(array_A)
	cdef double min_val   = array_A[0]
	cdef int min_index = 0

	for i in range(N):
		if array_A[i] < min_val:
			min_val = array_A[i]
			min_index = i
	return min_index

#===================================================================================================
# Get min from an array of numbers
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
cdef min_cy(double[:] values):
	cdef int Nvals = len(values)
	cdef int i
	cdef double min_val
	min_val = 1e9
	for i in range(Nvals):
		if min_val > values[i]:
			min_val = values[i]
	return min_val

#===================================================================================================
# Distance between two locations on the earth
#===================================================================================================
# Cythonized version of the vicenty function by Maurycy Pietrzak: https://github.com/maurycyp/vincenty
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
cdef vincenty_cy(double lat1, double lon1, double lat2, double lon2):

	"""
	Parameter
	=========
	lat/lon: Site coordinates in deg.
	
	Returns
	=======
	Distance in km.
	"""
	
	cdef int    a = 6378137  # meters
	cdef double f = 1 / 298.257223563
	cdef double b = 6356752.314245
	cdef int max_iter = 200
	cdef double conv  = 1e-12
	cdef double sinLambda, cosLambda, sinSigma, cosSigma, sigma, sinAlpha, cosSqAlpha, C, LambdaPrev

	if (lat1-lat2) == 0 and (lon1-lon2) == 0:
		return 0.0

	lat1 = lat1*pi/180
	lat2 = lat2*pi/180
	lon1 = lon1*pi/180
	lon2 = lon2*pi/180

	cdef double U1     = atan((1-f)*tan(lat1))
	cdef double U2     = atan((1-f)*tan(lat2))
	cdef double Lambda = lon2-lon1
	cdef double L      = lon2-lon1
	cdef double sinU1  = sin(U1)
	cdef double cosU1  = cos(U1)
	cdef double sinU2  = sin(U2)
	cdef double cosU2  = cos(U2)

	for iteration in range(max_iter):
		sinLambda = sin(Lambda)
		cosLambda = cos(Lambda)
		sinSigma  = sqrt(pow(cosU2*sinLambda,2)+pow(cosU1*sinU2-sinU1*cosU2*cosLambda,2))
		
		if sinSigma == 0:
			return 0.0
		
		cosSigma   = sinU1*sinU2+cosU1*cosU2*cosLambda
		sigma      = atan2(sinSigma,cosSigma)
		sinAlpha   = cosU1*cosU2*sinLambda/sinSigma
		cosSqAlpha = 1-pow(sinAlpha,2)
		
		try:
			cos2SigmaM = cosSigma-2*sinU1*sinU2/cosSqAlpha
		except ZeroDivisionError:
			cos2SigmaM = 0
		C = f/16*cosSqAlpha*(4+f*(4-3*cosSqAlpha))
		LambdaPrev = Lambda
		Lambda     = L+(1-C)*f*sinAlpha*(sigma+C*sinSigma*(cos2SigmaM+C*cosSigma*(-1+2*pow(cos2SigmaM,2))))
		
		if abs(Lambda-LambdaPrev)<conv:
			break
	else:
		return None

	cdef double uSq    = cosSqAlpha*(pow(a,2)-pow(b,2))/pow(b,2)
	cdef double A      = 1+uSq/16384*(4096+uSq*(-768+uSq*(320-175*uSq)))
	cdef double B      = uSq/1024*(256+uSq*(-128+uSq*(74-47*uSq)))
	cdef double dSigma = B*sinSigma*(cos2SigmaM+B/4*(cosSigma*(-1+2*pow(cos2SigmaM,2))-B/6*cos2SigmaM*(-3+4*pow(sinSigma,2))*(-3+4*pow(cos2SigmaM,2))))
	cdef double s      = b*A*(sigma-dSigma)/1000

	return s

#===================================================================================================
# Supporting functions
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
def get_bearing_cy(double lat1, double lon1, double lat2, double lon2):
	cdef conv = pi/180
	lat1 = lat1*conv
	lon1 = lon1*conv
	lat2 = lat2*conv
	lon2 = lon2*conv
	cdef double y = sin(lon2-lon1)*cos(lat2) 
	cdef double x = cos(lat1)*sin(lat2)-sin(lat1)*cos(lat2)*cos(lon2-lon1)
	cdef double theta   = atan2(y,x)
	cdef double bearing = (theta+2*pi)%(2*pi) #RP - Edit that might lead to errors
	return bearing

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
cdef cll2xy(double flon, double flat, double[:] slon, double[:] slat):

	cdef double lat, lon, distance, bearing
	cdef int i       = 0
	cdef int N_sites = len(slon)
	cdef double[:] X = np.zeros(N_sites, dtype='float64')
	cdef double[:] Y = np.zeros(N_sites, dtype='float64')

	for lat,lon in zip(slat,slon):
		distance = vincenty_cy(flat,flon,lat,lon)
		bearing  = get_bearing_cy(flat,flon,lat,lon)
		X[i] = distance*sin(bearing)
		Y[i] = distance*cos(bearing)
		i += 1
	return X,Y

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
cdef d2t(P):

	cdef double a1, b1, c1, d1, e1, a2, b2, c2, d2, e2, detinv, s1, s2, t1, t2, f, dclst, dis1, dis2, dis3, dis4
	cdef int inside = 0
	cdef int iclst

	cdef double[:] B        = np.zeros(3, dtype = 'float64')
	cdef double[:] E0       = np.zeros(3, dtype = 'float64')
	cdef double[:] E1       = np.zeros(3, dtype = 'float64')
	cdef double[:,:] E_clst = np.zeros([3,4], dtype = 'float64')

	P_clst = []

	B[0]  = P[0,0]
	B[1]  = P[1,0]
	B[2]  = P[2,0]
	E0[0] = P[0,1]-B[0]
	E0[1] = P[1,1]-B[1]
	E0[2] = P[2,1]-B[2]
	E1[0] = P[0,3]-B[0]
	E1[1] = P[1,3]-B[1]
	E1[2] = P[2,3]-B[2]
	a1 = E0[0]*E0[0]+E0[1]*E0[1]+E0[2]*E0[2]
	b1 = E0[0]*E1[0]+E0[1]*E1[1]+E0[2]*E1[2]
	c1 = E1[0]*E1[0]+E1[1]*E1[1]+E1[2]*E1[2]
	d1 = E0[0]*B[0]+E0[1]*B[1]+E0[2]*B[2]
	e1 = E1[0]*B[0]+E1[1]*B[1]+E1[2]*B[2]

	detinv = 1/(a1*c1-b1*d1)
	s1     = (b1*e1-c1*d1)*detinv
	t1     = (b1*d1-a1*e1)*detinv

	if isinf(detinv) == 0 and s1 >= 0 and s1 <= 1 and t1 >= 0 and t1 <= 1 and s1+t1 <= 1:
		inside = 1
		P_clst.append(B[0]+s1*E0[0]+t1*E1[0])
		P_clst.append(B[1]+s1*E0[1]+t1*E1[1])
		P_clst.append(B[2]+s1*E0[2]+t1*E1[2])
		dclst = P_clst[0]**2+P_clst[1]**2+P_clst[2]**2
		dclst = (dclst)**0.5
		return dclst, P_clst

	B[0]  = P[0,2]
	B[1]  = P[1,2]
	B[2]  = P[2,2]
	E0[0] = P[0,1]-B[0]
	E0[1] = P[1,1]-B[1]
	E0[2] = P[2,1]-B[2]
	E1[0] = P[0,3]-B[0]
	E1[1] = P[1,3]-B[1]
	E1[2] = P[2,3]-B[2]
	a2 = E0[0]*E0[0]+E0[1]*E0[1]+E0[2]*E0[2]
	b2 = E0[0]*E1[0]+E0[1]*E1[1]+E0[2]*E1[2]
	c2 = E1[0]*E1[0]+E1[1]*E1[1]+E1[2]*E1[2]
	d2 = E0[0]* B[0]+E0[1]* B[1]+E0[2]* B[2]
	e2 = E1[0]* B[0]+E1[1]* B[1]+E1[2]* B[2]

	detinv = 1/(a2*c2-b2*b2)
	s2 = (b2*e2-c2*d2)*detinv
	t2 = (b2*d2-a2*e2)*detinv

	if isinf(detinv) == 0 and s2 >= 0 and s2 <= 1 and t2 >= 0 and t2 <= 1 and s2+t2 <= 1:
		inside = 2
		P_clst.append(B[0]+s2*E0[0]+t2*E1[0])
		P_clst.append(B[1]+s2*E0[1]+t2*E1[1])
		P_clst.append(B[2]+s2*E0[2]+t2*E1[2])
		dclst = P_clst[0]**2+P_clst[1]**2+P_clst[2]**2
		dclst = (dclst)**0.5
		return dclst, P_clst

	if -d1 < 0:
		f = 0
	elif -d1 > a1:
		f = 1
	else:
		f = -d1/a1

	E_clst[0,0] = P[0,0]+f*(P[0,1]-P[0,0])
	E_clst[1,0] = P[1,0]+f*(P[1,1]-P[1,0])
	E_clst[2,0] = P[2,0]+f*(P[2,1]-P[2,0])

	if d2 < 0:
		f = 0
	elif -d2 > a2:
		f = 1
	else:
		f = -d2/a2

	E_clst[0,1] = P[0,2]+f*(P[0,1]-P[0,2])
	E_clst[1,1] = P[1,2]+f*(P[1,1]-P[1,2])
	E_clst[2,1] = P[2,2]+f*(P[2,1]-P[2,2])

	if -e2 < 0:
		f = 0
	elif -e2 > c2:
		f = 1
	else:
		f = -e2/c2

	E_clst[0,2] = P[0,2]+f*(P[0,3]-P[0,2])
	E_clst[1,2] = P[1,2]+f*(P[1,3]-P[1,2])
	E_clst[2,2] = P[2,2]+f*(P[2,3]-P[2,2])

	if -e1 < 0:
		f = 0
	elif -e1 > c1:
		f = 1
	else:
		f = -e1/c1

	E_clst[0,3] = P[0,0]+f*(P[0,3]-P[0,0])
	E_clst[1,3] = P[1,0]+f*(P[1,3]-P[1,0])
	E_clst[2,3] = P[2,0]+f*(P[2,3]-P[2,0])
	dis1 = E_clst[0,0]**2+E_clst[1,0]**2+E_clst[2,0]**2
	dis2 = E_clst[0,1]**2+E_clst[1,1]**2+E_clst[2,1]**2
	dis3 = E_clst[0,2]**2+E_clst[1,2]**2+E_clst[2,2]**2
	dis4 = E_clst[0,3]**2+E_clst[1,3]**2+E_clst[2,3]**2

	dis_seq = [dis1, dis2, dis3, dis4]
	dclst = np.nanmin(dis_seq)
	iclst = np.argmin(dis_seq)
	dclst = (dclst)**0.5
	P_clst.append(E_clst[0,iclst])
	P_clst.append(E_clst[1,iclst])
	P_clst.append(E_clst[2,iclst])

	return dclst,P_clst

#===================================================================================================
# Joyner-Boore distance
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
def get_Rjb_cy(	double[:] slat, double[:] slon,
				double flat1, double flon1, double flat2, double flon2,
				double fwidth, double fdip, double fZtor):
		
	"""
	Parameter
	=========
	slat/slon: Site coordinates in deg.
	flat1/flon1: Fault ULC coordinates in deg.
	flat2/flon2: Fault URC coordinates in deg.
	fwidth: Fault width in km.
	fdip: Fault dip in deg.
	fZtor: Depth to top of fault rupture in km.
	
	Returns
	=======
	Joyner-Boore distance.
	"""

	cdef int N_sites    = len(slat)
	cdef double conv    = pi/180
	cdef double[:] Rrup = np.zeros(N_sites, dtype = 'float64')
	cdef double[:] Rjb  = np.zeros(N_sites, dtype = 'float64')
	cdef double[:,:] pt = np.zeros([3,4], dtype = 'float64')
	cdef double botd    = fZtor + fwidth*sin(fdip*conv)
	cdef double rwh     = fwidth*cos(fdip*conv)
	cdef double fstrike, tmp_fstrike, dX, dY
	cdef int i_sta

	fdipDir = ''
	Sxy1    = cll2xy(flon1,flat1,slon,slat)
	Sxy2    = cll2xy(flon2,flat2,slon,slat)

	for i_sta in range(N_sites):
		pt[0,0] = -Sxy1[0][i_sta]
		pt[1,0] = -Sxy1[1][i_sta]
		pt[2,0] = 0.0
		pt[0,1] = -Sxy2[0][i_sta]
		pt[1,1] = -Sxy2[1][i_sta]
		pt[2,1] = 0.0

		if fdipDir == '':
			dX = pt[0,1]-pt[0,0]
			dY = pt[1,1]-pt[1,0]
			tmp_fstrike = atan(dY/dX)/conv
			if dX == 0 and dY > 0:
				fstrike = 0
			elif dX == 0 and dY < 0:
				fstrike = 180
			elif dX > 0:
				fstrike = 90-tmp_fstrike
			elif dX < 0:
				fstrike = 270-tmp_fstrike

			if fstrike + 90 >= 360:
				fdipDir = fstrike+90-360
			else:
				fdipDir = fstrike+90

		dX = rwh*sin(fdipDir*conv)
		dY = rwh*cos(fdipDir*conv)
		pt[0,2] = pt[0,1]+dX
		pt[1,2] = pt[1,1]+dY
		pt[2,2] = 0.0
		pt[0,3] = pt[0,0]+dX
		pt[1,3] = pt[1,0]+dY
		pt[2,3] = 0.0
		a = d2t(pt)
		Rjb[i_sta] = a[0]

	return np.asarray(Rjb)

#===================================================================================================
# Rupture distance
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
def get_Rrup_cy(	double[:] slat, double[:] slon,
				double flat1, double flon1, double flat2, double flon2,
				double fwidth, double fdip, double fZtor):
		
	"""
	Parameter
	=========
	slat/slon: Site coordinates in deg.
	flat1/flon1: Fault ULC coordinates in deg.
	flat2/flon2: Fault URC coordinates in deg.
	fwidth: Fault width in km.
	fdip: Fault dip in deg.
	fZtor: Depth to top of fault rupture in km.
	
	Returns
	=======
	Rupture distance.
	"""

	cdef int N_sites    = len(slat)
	cdef double conv    = pi/180
	cdef double[:] Rrup = np.zeros(N_sites, dtype = 'float64')
	cdef double[:] Rjb  = np.zeros(N_sites, dtype = 'float64')
	cdef double[:,:] pt = np.zeros([3,4], dtype = 'float64')
	cdef double botd    = fZtor + fwidth*sin(fdip*conv)
	cdef double rwh     = fwidth*cos(fdip*conv)
	cdef double fstrike, tmp_fstrike, dX, dY
	cdef int i_sta
	
	fdipDir = ''
	Sxy1    = cll2xy(flon1,flat1,slon,slat)
	Sxy2    = cll2xy(flon2,flat2,slon,slat)

	for i_sta in range(N_sites):
		pt[0,0] = -Sxy1[0][i_sta]
		pt[1,0] = -Sxy1[1][i_sta]
		pt[2,0] = -fZtor
		pt[0,1] = -Sxy2[0][i_sta]
		pt[1,1] = -Sxy2[1][i_sta]
		pt[2,1] = -fZtor

		if fdipDir == '':
			dX = pt[0,1]-pt[0,0]
			dY = pt[1,1]-pt[1,0]
			tmp_fstrike = atan(dY/dX)/conv
			if dX == 0 and dY > 0:
				fstrike = 0
			elif dX == 0 and dY < 0:
				fstrike = 180
			elif dX > 0:
				fstrike = 90-tmp_fstrike
			elif dX < 0:
				fstrike = 270-tmp_fstrike
			if fstrike + 90 >= 360:
				fdipDir = fstrike+90-360
			else:
				fdipDir = fstrike+90

		dX = rwh*sin(fdipDir*conv)
		dY = rwh*cos(fdipDir*conv)
		pt[0,2] = pt[0,1]+dX
		pt[1,2] = pt[1,1]+dY
		pt[2,2] = -botd
		pt[0,3] = pt[0,0]+dX
		pt[1,3] = pt[1,0]+dY
		pt[2,3] = -botd
		a = d2t(pt)
		Rrup[i_sta] = a[0]

	return np.asarray(Rrup)

#===================================================================================================
# Rx
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
def get_Rx_cy(	double[:] slat, double[:] slon, double flat1, double flon1, double flat2, double flon2):

	"""
	Parameter
	=========
	slat/slon: Site coordinates in deg.
	flat1/flon1: Fault ULC coordinates in deg.
	flat2/flon2: Fault URC coordinates in deg.
	
	Returns
	=======
	Rx distance.
	"""
	
	cdef int N_sites = len(slon)
	cdef double[:] Rx = np.zeros(N_sites, dtype='float64')
	cdef int i
	
	for i in range(N_sites):
		frame   = nv.FrameE(a=6371008.8, f=0)
		pointA1 = frame.GeoPoint(flat1,flon1,degrees=True)
		pointA2 = frame.GeoPoint(flat2,flon2,degrees=True)
		pointB  = frame.GeoPoint(slat[i],slon[i],degrees=True)
		pathA   = nv.GeoPath(pointA1, pointA2)
		Rx[i]   = pathA.cross_track_distance(pointB, method='greatcircle')/1000
	
	return np.asarray(Rx)

#===================================================================================================
# Get all distances (convenient to handle multi-segment fault)
#===================================================================================================
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
@cython.cdivision(True)
def get_distances_cy(	double[:] site_lat,double[:] site_lon,double[:] ULC_lat,double[:] ULC_lon,double[:] URC_lat,double[:] URC_lon,
						double[:] segm_width,double[:] segm_length,double[:] segm_dip,double[:] segm_strike,double[:] segm_Ztor):
	
	"""
	Parameter
	=========
	site_lat/site_lon: Site coordinates in deg.
	ULC_lat/ULC_lon: Fault ULC coordinates in deg.
	URC_lat/URC_lon: Fault URC coordinates in deg.
	segm_width: Fault segment width in km. Array if multi-segment fault.
	segm_length: Fault segment length in km. Array if multi-segment fault.
	segm_dip: Fault segment dip in deg. Array if multi-segment fault.
	segm_strike: Fault segment strike in deg. Array if multi-segment fault.
	segm_Ztor: Fault segment depth to top of rupture ni km. Array if multi-segment fault.
	
	Returns
	=======
	Joyner-Boore, rupture, and Rx distances.
	"""
	
	cdef int N_segms = len(segm_dip)
	cdef int N_sites = len(site_lat)
	cdef double[:,:] tmp_Rjb  = np.zeros((N_sites,N_segms), dtype='float64')
	cdef double[:,:] tmp_Rrup = np.zeros((N_sites,N_segms), dtype='float64')
	cdef double[:,:] tmp_Rx   = np.zeros((N_sites,N_segms), dtype='float64')
	cdef double[:] ALL_Rjb    = np.zeros(N_sites, dtype='float64')
	cdef double[:] ALL_Rrup   = np.zeros(N_sites, dtype='float64')
	cdef double[:] ALL_Rx     = np.zeros(N_sites, dtype='float64')
	cdef double[:] slat, slon
	cdef int i 

	for i in range(N_segms):
		for j in range(N_sites):
			slat = np.array([site_lat[j]])
			slon = np.array([site_lon[j]])
			tmp_Rjb[j][i]  = get_Rjb_cy(slat,slon,ULC_lat[i],ULC_lon[i],URC_lat[i],URC_lon[i],segm_width[i],segm_dip[i],segm_strike[i])[0]
			tmp_Rrup[j][i] = get_Rrup_cy(slat,slon,ULC_lat[i],ULC_lon[i],URC_lat[i],URC_lon[i],segm_width[i],segm_dip[i],segm_Ztor[i])[0]
			tmp_Rx[j][i]   = get_Rx_cy(slat,slon,ULC_lat[i],ULC_lon[i],URC_lat[i],URC_lon[i])[0]

	for j in range(N_sites):
		ALL_Rjb[j]  = min(tmp_Rjb[j][:])
		ALL_Rrup[j] = min(tmp_Rrup[j][:])
		ALL_Rx[j]   = tmp_Rx[j][argmin_cy(tmp_Rjb[j][:])]

	return np.asarray(ALL_Rjb),np.asarray(ALL_Rrup),np.asarray(ALL_Rx)
