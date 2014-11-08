#-------------------------------------------------------------------------------
# Name:        ball2
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

def y(t):
    return v0*t-0.5*g*t**2

v0 = [20.0,5.0,15.0,25.0]
g = 9.81

t=np.linspace(-50,50)
y=(v0[0]*t)-(g*(t**2)*0.5)

max_y = max(y)
max_x = t[y.argmax()]
print "Maximum height, V0 = 20.0: ",max_y, " m"

plt.xlabel("time (s)")
plt.ylabel("position (m)")
plt.plot(t, y, 'ro')

# V0 = 5.0

y1=(v0[1]*t)-(g*(t**2)*0.5)

max_y1 = max(y)  # Find the maximum y value
max_x1 = t[y.argmax()]  # Find the x value corresponding to the maximum y value
print "Maximum height, V0 = 5.0: ",max_y1, " m"

plt.plot(t, y1, 'b--')

# V0 = 15.0

y2=(v0[2]*t)-(g*(t**2)*0.5)

max_y2 = max(y)  # Find the maximum y value
max_x2 = t[y.argmax()]  # Find the x value corresponding to the maximum y value
print "Maximum height, V0 = 15.0: ",max_y2, " m"

plt.plot(t, y2, 'yo')

# V0 = 25.0

y3=(v0[3]*t)-(g*(t**2)*0.5)

max_y3 = max(y)  # Find the maximum y value
max_x3 = t[y.argmax()]  # Find the x value corresponding to the maximum y value
print "Maximum height, V0 = 25.0: ",max_y3, " m"

plt.plot(t, y3, 'g--')
plt.show()