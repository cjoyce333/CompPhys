#-------------------------------------------------------------------------------
# Name:        karate
# Purpose:
#
# Author:      Clarissa Joyce
#
# Created:     17/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import numpy as np
from math import *
import matplotlib.pyplot as plt

data = np.loadtxt("Karate.txt")

t=data[:,0]
p=data[:,1]

print len(t)

v=[]
a=[]
d=[]

for i in range(0,len(p)-1):
    n=p[i+1]-p[i]
    d.append(n)

v.append(0)
for i in range(0,len(t)-1):
    n=d[i]/t[i]
    v.append(n)
#print len(v)

a.append(0)
for i in range(0,len(v)-1):
    n=(v[i+1]-v[i])/2
    a.append(n)
#print len(a)


m=max(v)
print "The max velocity of the hand is: ",m

mvp = p[v.index(max(v))]
print "The hand is at ",mvp

ma = max(a)
g=ma/9.8
print "The max acceleration of the hand is: ",ma,"or ",g,"g's"

mxp = p[a.index(max(a))]
print "The hand is at ",mxp


np.savetxt("karate2.txt", np.column_stack((v,a)),delimiter="," )#, header='Velocity, Acceleration')

plt.xlabel("time (s)")
plt.ylabel("position(m), velocity(m/s), acceleration(m/s^2")

plt.plot(p,t,"bo")
plt.plot(v,t,"ro")
plt.plot(a,t,"g*")

plt.show()