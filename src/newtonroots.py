#-------------------------------------------------------------------------------
# Name:        newtonroots.py
# Purpose:
#
# Author:      Claire
#
# Created:     25/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from scipy.optimize import*

def f(x):
    return 3.5*x*x*x -2.1*x*x +5.1*x -3

print newton(f,1.2)