#-------------------------------------------------------------------------------
# Name:        cart
# Purpose:
#
# Author:      Claire Joyce
#
# Created:     14/10/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import matplotlib.pyplot as plt
from math import *

m0 = 10.0 #initial mass of cart and contents
v = 30. #initial velocity
t = 0. #initial time
x = 0. #initial position
dt = 0.01 # time step
R = 5.0 #rate of falling rain/rate at which cart gains mass

def accel(v,t):
    return -v*R/m(t)

def m(t): #define mass at any time
    return R*t +m0

def p(t): #the momentum at any time
    return m(t)*v

while t<10.00:
    #simple euler
    v += accel(v,t)*dt
    x += v*dt

    plt.figure(1)
    plt.suptitle("Moving cart taking on mass")
    plt.plot(t,x,'bo')
    plt.xlabel("Time(s)")
    plt.ylabel("Position (m)")

    plt.figure(2)
    plt.suptitle("Moving cart taking on mass")
    plt.plot(t,v,'ro')
    plt.xlabel("Time(s)")
    plt.ylabel("Velocity (m/s)")

    plt.figure(3)
    plt.suptitle("Moving cart taking on mass")
    plt.plot(t,p(t),'go')
    plt.xlabel("Time(s)")
    plt.ylabel("Momentum (kg m/s)")

    t+=dt

plt.show()