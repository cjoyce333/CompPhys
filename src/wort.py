#-------------------------------------------------------------------------------
# Name:        wort
# Purpose:
#
# Author:      Claire Joyce
#
# Created:     25/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from math import *
import matplotlib.pyplot as plt
from numpy import *

t0f=212
t0c=100
tsf=70
tsc=21
m=40
s=1200
h=12
c=4200
q=-3600
T=100
dt=0.1
t=0


def f(T):
    return (q-h*s*(T-tsc))/(m*c)

plt.xlabel("time s")
plt.ylabel("Temp C")
while (T>=40):
    plt.plot(t,T,"bo")
    endT=T+f(T)*dt
    T+=(f(T)+f(endT))*dt/2.
    t=t+dt


print "Time= ",t," s"
plt.show()
