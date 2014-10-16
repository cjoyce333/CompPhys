#-------------------------------------------------------------------------------
# Name:        spring
# Purpose:
#
# Author:      Clarissa Joyce
#
# Created:     17/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from numpy import *
from math import *
import matplotlib.pyplot as plt
import numpy as np

m = np.arange(0.2,1.0,0.1)
y = [4.9,5.3,5.7,6.7,7.2,7.5,8.4,9.2]
g=9.8

#m[0]*g=k*(y-y0)

# initialize sums
sum_m = 0
sum_y = 0
sum_mm = 0
sum_my = 0
mmin = 0

#perform our calculations
for i in range(0,len(m)):
    sum_m = sum_m+m[i-1]
    sum_y = sum_y+y[i-1]
    mm = m[i-1]*m[i-1]
    sum_mm = sum_mm +mm
    my = m[i-1]*y[i-1]
    sum_my = sum_my+my

#calculate the coefficients
D = len(m)*sum_mm - sum_m*sum_m
A= (sum_mm*sum_y - sum_m*sum_my)/D
B= (len(m)*sum_my-sum_m*sum_y)/D

#plot data points
plt.plot(m,y,"bo")

#plot least squares fit line
xc= linspace(mmin,m[len(m)-1],10)
yc= A+B*xc

y0 = A+B
k= m*g/(y-y0)

print "y0 = ",y0,", k = ",k

plt.plot(xc,yc,"r-")
plt.show()