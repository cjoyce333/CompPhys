#-------------------------------------------------------------------------------
# Name:        quantumparticles
# Purpose:
#
# Author:      Claire Joyce
#
# Created:     10/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

list=[]
for n1 in range(1,11,1):
    for n2 in range (1,11,1):
        for n3 in range (1,11,1):
            E= n1**2 + n2**2 + n3**2
            list.append(E)
list.sort()
print list