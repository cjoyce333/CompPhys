#-------------------------------------------------------------------------------
# Name:        temperatures
# Purpose:
#
# Author:      Claire
#
# Created:     25/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from math import *
import matplotlib.pyplot as plt
from numpy import *

Ti=input("Initial temp of apt (F): ")
r=0.1
t=input("Time period (hours): ")
t0=0
dt=0.1

x=[]
yI=[]
yS=[]
E=[]

def f(xt):
    return 92.-10.*sin(2.*math.pi*(xt+3.)/24.)


def g(xt):
    TS=f(xt)
    return TS+(Ti-TS)*math.e**(-r*xt)
#TA=g(xt)


#T=(Ti-TS)/TS

plt.xlabel("time t")
plt.ylabel("Temp")

while t0<t:
   # tm=T+(-r*(T-g(t))*dt/2.)
   # T=T+(-r*(tm-f(t))*dt/2.)
    x.append(t0)
    yI.append(g(t0))
    yS.append(f(t0))
    plt.plot(t0,f(t0),"bo")
    plt.plot(t0,g(t0),"r+")

    t0+=dt

for i in range(0,len(yS)):
    for j in range(0,len(yI)):
        if(yI[j]==yS[i]):
            E.append(x[j])


maxy=max(yI)
print "Maximum temp inside= ",maxy

print "Temps equal at time(s): ",E, "h"

print "Inside leads for 40 hours."

plt.show()