#-------------------------------------------------------------------------------
# Name:        geiger
# Purpose:
#
# Author:      Clarissa Joyce
#
# Created:     17/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt


data = [10,12,15,8,13,14,19,18,11,13,7,8,11,8,12,6,13,8,6]

mean = np.mean(data)
sigma=np.std(data)

difference = abs(sigma - mean**0.5)
if (difference<1):
    print "The values of sigma and the square root of the mean are close"
else:
    print "The values of sigma and the square root of the mean are not close"
num_bins=100
plt.hist(data,num_bins,facecolor='green')
plt.show()

print "Mean=",mean, ", Sigma=",sigma, ", Difference= ",difference