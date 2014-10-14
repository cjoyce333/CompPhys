#-------------------------------------------------------------------------------
# Name:        leastsquaresplot
# Purpose:
#
# Author:      Claire Joyce
#
# Created:     16/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from numpy import *
from math import *
import matplotlib.pyplot as plt

# get number of data points
N = input("enter number of data points")

# initialize sums
sum_x = 0
sum_y = 0
sum_xx = 0
sum_xy = 0
xmin = 0

#initialize lists
x = []
y = []

#get data vals from user
for i in range(0,N+1):
    print "for point %s"%i
    x.append(input("enter x:"))
    y.append(input("enter y:"))

#perform our calculations
for i in range(0,N+1):
    if x[i-1] < xmin:
        xmin = x[i-1]
    sum_x = sum_x+x[i-1]
    sum_y = sum_y+y[i-1]
    xx = x[i-1]*x[i-1]
    sum_xx = sum_xx +xx
    xy = x[i-1]*y[i-1]
    sum_xy = sum_xy+xy

#calculate the coefficients
D = N*sum_xx - sum_x*sum_x
A= (sum_xx*sum_y - sum_x*sum_xy)/D
B= (N*sum_xy-sum_x*sum_y)/D

#plot data points
plt.plot(x,y,"bo")

#plot least squares fit line
xc= linspace(xmin,x[N-1],10)
yc= A+B*xc

plt.plot(xc,yc,"r-")

print "the fitted straight line is y= (%s) + %sx"%(A,B)



