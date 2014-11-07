#-------------------------------------------------------------------------------
# Name:        pitch
# Purpose:
#
# Author:      Claire Joyce
#
# Created:     27/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from numpy import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

data = np.loadtxt("pitchfx_data-FIXED.txt", skiprows = 2,usecols=(25,27,28,29,32,33,34,35,36,37,38,39,40))

x0=data[:,4]
print x0
y0=data[:,5]
z0=data[:,6]

tstart=data[:,0]
ftime=data[:,1]

vx0=data[:,7]
vy0=data[:,8]
vz0=data[:,9]
ax=data[:,10]
ay=data[:,11]
az=data[:,12]

finx=data[:,2]
finz=data[:,3]

N=int(ftime[0]*100)

x = zeros(N,float)
y = zeros(N,float)
z = zeros(N,float)
x[0],y[0],z[0] = (x0[0],y0[0],z0[0])

print x0[0]
print vx0[0]
print ax[0]
for i in range(0, len(x)):
    t = i/100.

    x[i] = x0[0] +vx0[0]*t + 0.5*ax[0]*t**2
    y[i] = y0[0] +vy0[0]*t + 0.5*ay[0]*t**2
    z[i] = z0[0] +vz0[0]*t + 0.5*az[0]*t**2

#plotting in 3D
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x,y,z)
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")
ax.set_zlabel("z axis")

plt.plot(finx,finz,"go")

plt.show()
