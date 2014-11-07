#-------------------------------------------------------------------------------
# Name:        sinesum
# Purpose:
#
# Author:      Claire
#
# Created:     08/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import math
import numpy
from math import pi

x=input("enter value of x in degrees:")
x= x*pi/180
n=input("number terms to calculate:")

sine1 = math.sin(x)
print sine1

sum=0
for n in range(0,n+1,1):
    sum =sum +(((-1)**n)*((x**n)/math.factorial(n)))

print sum
error = ((sine1-sum)/sine1)
print "error:", error
