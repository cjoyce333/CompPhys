#-------------------------------------------------------------------------------
# Name:        quadratic
# Purpose:
#
# Author:      Claire Joyce
#
# Created:     08/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

a=2; i=1; c=2
from math import sqrt
import cmath
q=sqrt(abs(i*i - 4*a*c))
x1 = (-i+q)/2*a
x2 = (-i-q)/2*a
print x1,x2

#the program did not support complex numbers