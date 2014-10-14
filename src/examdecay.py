#-------------------------------------------------------------------------------
# Name:        examdecay
# Purpose:
#
# Author:      Claire Joyce
#
# Created:     27/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from math import *
import matplotlib.pyplot as plt

k1=5.76*10**(-11)
k2=4.85*10**(-10)

To=0
T=4.5*10**9
x = 0

K0=10000
Ar0=0
Ca0=0

h=10**7

def dK(K):
    return -(k1+k2)*K

def dAr(K):
    return k1*K

def dCa(K):
    return k2*K

AA=[]
KK=[]

while To<T:
    plt.plot(To,K0,"bo")
    plt.plot(To,Ar0,"r+")
    plt.plot(To,Ca0,"go")

    Kend=K0-k1*dK(K0)*h
    K0+=(dK(K0)+dK(Kend))*h/2.0

    Arend=Ar0 + dAr(K0)*h
    Ar0+=(dAr(K0)+dAr(Arend))*h/2.0

    Caend=Ca0 + dCa(K0)*h
    Ca0+=(dCa(K0)+dCa(Caend))*h/2.
    AA.append(abs(round(dAr(Ar0)/dK(K0),4)))

    #KK.append(round(dK(K0),3))
    To=To+h
#print AA,"\n",KK

ratio=3.900*10**-3
'''
for i in range(0,len(AA)):
    print AA[i]
'''
year=(AA.index(ratio))*10**7
print "Age of T-rex: ",year," years"

plt.title("Radioactive decay of K, Ar, and Ca")
plt.xlabel("Years")
plt.ylabel("Number atoms")
plt.show()