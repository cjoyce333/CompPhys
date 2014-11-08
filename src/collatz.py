#-------------------------------------------------------------------------------
# Name:        collatz
# Purpose:
#
# Author:      Claire Joyce
#
# Created:     10/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from math import *
from scipy import *
from numpy import *

n=input("natural number:")

for i in range(0,20):
    while n!=1:
        if n%2 ==0:n=n/2
        else: n= 3*n+1
        print n

