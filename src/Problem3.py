#-------------------------------------------------------------------------------
# Name:        Problem3
# Purpose:
#
# Author:      Claire Joyce
#
# Created:     08/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

V0=3
t=2
a=2
x=V0*t
x+=(1./2)*a*t**2 # python is case sensitive, so this v0 must be capitalized

print a
print x # from the original problem, python gets x=6, when the answer should be ten.
        # this is because the fraction 1/2 is not interpreted correctly by python.
        # The numbers must be given float values to be used