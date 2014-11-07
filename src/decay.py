#-------------------------------------------------------------------------------
# Name:        decay
# Purpose:
#
# Author:      Claire JOyce
#
# Created:     25/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from numpy import *
from math import *
import matplotlib.pyplot as plt
import numpy as np

k=input("enter decay constant k= ")

N=1000
t=0
t_stop=100
h= input("val of time step,h")

plt.title("Euler method of solution")
plt.xlabel("time t")

fig = plt.figure()
ax=fig.add_subplot(2,1,1)

while t<t_stop:
    plt.plot(t,N,"bo")

    N=N-k*N*h
    t=t+h

ax.set_xscale('log')
plt.show()