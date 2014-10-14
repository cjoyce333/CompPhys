#-------------------------------------------------------------------------------
# Name:        interest
# Purpose:     to calculate the value of a bank account after a given amount of years
#
# Author:      Claire Joyce
#
# Created:     08/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

origval = 1000
interestperyear = 0.025
n = [5,10,30]

newval = origval*(1+interestperyear)**n[0]
print "The account value after " + repr(n[0]) + " years is $"+ repr(newval) +"."

newval = newval*(1+interestperyear)**n[1]
print "The account value after " + repr(n[1]) + " years is $"+ repr(newval) +"."

newval = newval*(1+interestperyear)**n[2]
print "The account value after " + repr(n[2]) + " years is $"+ repr(newval) +"."
