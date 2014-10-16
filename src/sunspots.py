#-------------------------------------------------------------------------------
# Name:        sunspots
# Purpose:
#
# Author:      Claire
#
# Created:     09/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from numpy import loadtxt
from pylab import scatter, xlabel,ylabel,xlim,ylim,show

data=loadtxt("stars.txt", float)
x=data[:,0] # : means all vals
y=data[:,1]

scatter(x,y)
xlabel("temperature")
ylabel("ab mag")
xlim(0,13000)
ylim(-5,20)
show()