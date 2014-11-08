#-------------------------------------------------------------------------------
# Name:        daughterdecay
# Purpose:
#
# Author:      Claire Joyce
#
# Created:     25/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from numpy import *
from math import *
import matplotlib.pyplot as plt
import numpy as np

N1=1000
N2=0
t=0
t_stop=60

t1=input("t1")
t2=input("t2")
h=input("val time step h")

k1=math.log(2,math.e)/t1
k2=math.log(2,math.e)/t2

plt.title("Heun's Method of Solution")
plt.xlabel("time t")
plt.ylabel("N(t)")

def f1(N1):
    return -k1*N1

def f2(N1,N2):
    return k1*N1-k2*N2

while t<t_stop:
    plt.plot(t,N1,"bo")
    plt.plot(t,N2,"r+")

    N1_end=N1-k1*N1*h # use euler to find the val of N1 at end of interval
    N2_end=N2 + (k2*N1 - k2*N2)*h # use euler to find the val of N2 at end of interval

    N2=N2+(f2(N1,N2)+f2(N1_end,N2_end))*h/2.0
    N1=N1+(f1(N1)+f1(N1_end))*h/2.0
    t=t+h

a=N1_end/N1
i=N2_end/N1
c=N2_end*k2

print "When t=60s:\na=",a,"\nb=",i,"\nc=",c


plt.show()
