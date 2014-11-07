#-------------------------------------------------------------------------------
# Name:        Q1d
# Purpose:
#
# Author:      Clarissa Joyce
#
# Created:     27/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python
from math import exp, sin
def expsin(x,p,q):
    return exp(p*x)*sin(q*x)

def f(x,m,n,r,s):
    return expsin(x,r,m)+expsin(x,s,n)
x=2.5
print "The corrected output is: ", f(x,0.1,0.2,1,1)

#Imports must come before they are used.
#Functions must be defined before they are called.