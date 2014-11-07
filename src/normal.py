#-------------------------------------------------------------------------------
# Name:        normal
# Purpose:
#
# Author:      Clarissa Joyce
#
# Created:     17/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from numpy import *
import matplotlib.pyplot as plt
import numpy as np

#sigma describes the width of the distribution

mean=0
x=range(-5,6,1)
sigma = [0.5,1.0,2.0]

p1=[]
p2=[]
p3=[]

for j in x:
    G=(1.0/(sigma[0]*((2.*pi)**(0.5))))*(np.e**(-(x[j]-mean)**2/(2.0*sigma[0]**2.)))
    G=-math.log10(G)
    p1.append(G)

for j in x:
    G=(1.0/(sigma[1]*((2.*pi)**(0.5))))*(np.e**(-(x[j]-mean)**2/(2.0*sigma[1]**2.)))
    G=-math.log10(G)
    p2.append(G)

for j in x:
    G=(1.0/(sigma[2]*((2.*pi)**(0.5))))*(np.e**(-(x[j]-mean)**2/(2.0*sigma[2]**2.)))
    G=-math.log10(G)
    p3.append(G)

plt.xlabel("x/sigma")
plt.ylabel("G(X) (log10 scaled)")

plt.plot(x,p1,"r--")
plt.plot(x,p2,"b--")
plt.plot(x,p3,"y--")

plt.show()
