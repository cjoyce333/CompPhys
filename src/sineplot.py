#####
#
#sineplot.py
#09/04/14
#plotting program v0
#
#####

#import matplotlib
#import matplotlib.pyplot as plt
#from numpy import *
from scipy import *

x = arange(-pi,pi,pi/100) #list is 1D array
plt.plot(x, sin(x), "b-", label = 'sine')
plt.plot(x,cos(x),"r-.", label = 'cosine')
plt.xlabel('x vals')
plt.ylabel('trig function vals')
plt.xlim(-pi,pi)
plt.ylim(-1,1)
plt.legend(loc='upper right')

plt.show()
