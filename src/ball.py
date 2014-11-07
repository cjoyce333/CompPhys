#-------------------------------------------------------------------------------
# Name:        ball
# Purpose:
#
# Author:      Clarissa Joyce
#
# Created:     17/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from numpy import *
import matplotlib.pyplot as plt
import numpy as np

v0 = 20.0
g = 9.81

t=np.linspace(-50,50)
y=(v0*t)-(g*(t**2)*0.5)

max_y = max(y)  # Find the maximum y value
max_x = t[y.argmax()]  # Find the x value corresponding to the maximum y value
print "Maximum height: ",max_y, " m"

plt.xlabel("time (s)")
plt.ylabel("position (m)")
plt.plot(t, y, 'ro')
plt.show()