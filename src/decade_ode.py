'''
Created on Oct 14, 2014

@author: James
'''

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(x,t,k):
    return -k*x

t=np.arange(0.0,2.,0.01)
x0=10.0
k=5.0

x=odeint(f,x0,t,args=)

plt.plot(t, x)
plt.show()