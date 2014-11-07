#-------------------------------------------------------------------------------
# Name:        football
# Purpose:
#
# Author:      Claire Joyce
#
# Created:     10/10/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import matplotlib.pyplot as plt
from math import *

Vo = 30
Tv = 45
g = 9.81
xx = []
yy = []
thth = []
ranges = []
y = 2
#thstep = 1*pi/180

Maxt = 0
def euler(y, vy, vt ):
    t = 0
    dt = .1
    plt.xlabel("TIme (s)")
    plt.ylabel("Height(m)")
    while(y>=0):
        xx.append(t)
        yy.append(y)
        ay = -g*(1+vy*abs(vy)/(vt))
        vy = vy + ay*dt
        y = y + vy*dt
        t = t+dt
    Maxt = t

plt.xlabel("Angle")
plt.ylabel("Range")
plt.title("Tony Romo's throw range")

th = 0
while th<90:
    vy = Vo*sin(th*pi/180)
    euler(y, vy, Tv)
    vx = Vo * cos(th*pi/180)
    plt.plot(th,max(xx)*vx,'bo')
    thth.append(th)
    ranges.append(max(xx)*vx)

    th+=.5

maxRange = max(ranges)
optTheta = thth[ranges.index(max(ranges))]
print "Biggest range: ",maxRange
print "Optimum angle: ",optTheta
print "My results do not agree with the given observation."
plt.show()
