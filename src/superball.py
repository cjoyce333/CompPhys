#-------------------------------------------------------------------------------
# Name:        superball (4.3)
# Purpose:
#
# Author:      Claire Joyce
#
# Created:     07/10/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python


#The distances between impact points increase with each bounce.
#Air resistance causes a decrease in the height of each bounce.

#import libraries
import matplotlib.pyplot as plt
from math import *


#define and get initial condition and constants
g=9.81
h=input("Enter the height of the ball:")
theta = 30*pi/180.0 #conv to radians
v=sqrt(2*g*h) #init speed of ball at incline
vx=0
vy=-v
x=0
y=0
t=0
dt=0.01

while t<10:
    ay=-g
    vy+=ay*dt
    vx=vx
    y+=vy*dt
    x-=vx*dt

    yIncline=x*tan(theta)
    if y<=yIncline:
        print "new bounce"
        v=sqrt(vx**2+vy**2)
        vx=v*cos(theta)
        vy=v*sin(theta)
    t+=dt

    plt.plot(x,y,"c+")
    plt.plot(x,x*tan(theta),"bo")
    plt.xlabel("Position (x)")
    plt.ylabel("Position (y)")
    plt.title("Superball Bounce on Incline")

plt.show()
