#-------------------------------------------------------------------------------
# Name:        baseball
# Purpose:
#
# Author:      Claire Joyce
#
# Created:     16/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# use flight time and create an integer number of points for plotting
ftime = 0.30455 - 0.075662
N = int(ftime*100)

x = zeros(N,float)
y = zeros(N,float)
z = zeros(N,float)

# use initial values from spreadsheet
x[0],y[0],z[0] = (-1.61,55,6.512962)
vx0 = 5.965682
vy0 = -134.333
vz0 = -7.21297
a_x = -11.364
a_y = 28.807
a_z = -15.949

#step through points for plotting
for i in range(1, N, 1):
    t = i/100.
    x[i] = x[0] +vx0*t + 0.5*a_x*t**2
    y[i] = y[0] +vy0*t + 0.5*a_y*t**2
    z[i] = z[0] +vz0*t + 0.5*a_z*t**2

#plotting in 3D
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x,y,z)
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")
ax.set_zlabel("z axis")

plt.show()