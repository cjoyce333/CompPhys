#-------------------------------------------------------------------------------
# Name:        histogram
# Purpose:
#
# Author:      Claire Joyce
#
# Created:     11/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("sunspotnumber.txt",skiprows=1)
y=data[:,0]
m=data[:,1]
ssn=data[:,2]

t=y + m/12.0

plt.scatter(t,ssn)
plt.xlabel("Decimal Year")
plt.ylabel("Sunspot Number")
plt.grid()

plt.show()

mu = np.mean(ssn)
sigma=np.std(ssn)

print "the mean val is", mu
print "the standart dev is", sigma

num_bins=100
plt.hist(ssn,num_bins,facecolor='green')
plt.show()


# write to a txt file ssn and decimal year
np.savetxt("file.txt", np.column_stack((ssn,t)),delimiter=",", header="sunspot number, decimal year")
