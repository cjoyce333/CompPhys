#-------------------------------------------------------------------------------
# Name:        coldmedication
# Purpose:      solve diff eq for amount of cold meds in blood stream and GI as it goes through GI & bloodstream
#
# Author:      Claire
#
# Created:     25/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import matplotlib.pyplot as plt
from numpy import *
from math import *

#Initialize vals
t=0
tstop=120
h=0.01
I=0
x=0
y=0

k1=0.6931 #dissolving constang
k2=0.231 #clearing constant

xend=0
yend=0

def Rx(x,I):        #calc rate of absorption into GI
    return I-k1*x

def Ry(x,y):
    return k1*x-k2*y

plt.axis([0,tstop,0,7])

while t<tstop:
    if t%6 <= 6.5%6:
        I=12.
    else:
        I=0

    yend=y+Ry(x,y)*h #use euler to get end point
    y+=(Ry(x,y)+Ry(xend,yend))*h/2.0
    xend=x+Rx(x,I)*h
    x+= (Rx(x,I)+Rx(xend,I))*h/2.0
    plt.plot(t,x,"b+")
    plt.plot(t,y,"r+")
    t+=h
plt.xlabel("time h")
plt.ylabel("drugs mg")
plt.show()

#The graph shows that the medication in the GI and Bloodstream
#will spike with each pill taken, and then decrease gradually until more medecine is taken.
#The medecine must be taken about every six hours to maintain an effective amount.

#Michael will be asleep in physics class from the cold medicine.