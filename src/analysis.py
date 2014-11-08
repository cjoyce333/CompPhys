#-------------------------------------------------------------------------------
# Name:        analysis
# Purpose:
#
# Author:      Claire Joyce
#
# Created:     27/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import numpy as np
from numpy import *
from math import *
import matplotlib.pyplot as plt

data = np.loadtxt("extinctdata.txt",skiprows=1)

x=data[:,0]
y=data[:,1]
r=[]
a=np.mean(y)

for i in range(0,len(y)):
    r.append(y[i]-a)

s=np.std(y)
print len(y)
print len(r)
print "Average y val: ",a,"\nStandard Dev: ",s
# initialize sums
sum_x = 0
sum_y = 0
sum_xx = 0
sum_xy = 0
xmin = min(x)

#perform our calculations
for i in range(0,len(x)):
    sum_x = sum_x+x[i-1]
    sum_y = sum_y+y[i-1]
    xx = x[i-1]*x[i-1]
    sum_xx = sum_xx +xx
    xy = x[i-1]*y[i-1]
    sum_xy = sum_xy+xy

#calculate the coefficients
D = len(x)*sum_xx - sum_x*sum_x
A= (sum_xx*sum_y - sum_x*sum_xy)/D
B= (len(x)*sum_xy-sum_x*sum_y)/D

#plot data points
plt.subplot(211)
plt.plot(x,y,"bo")
plt.title("Least Squares Plot of Extinct Data")
plt.xlabel("Air Mass")
plt.ylabel("Magnitude")
plt.errorbar(x,y,s,marker='s',mfc='red', mec='green', ms=2, mew=1)
#plot least squares fit line
xc= linspace(xmin,max(x),100)
yc= A+B*xc
print "y=",B,"x","+",A
plt.plot(xc,yc,"r-")

plt.subplot(212)
plt.plot(x,r,"go")
plt.xlabel("Air Mass")
plt.ylabel("Magnitude")

plt.show()