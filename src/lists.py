#-------------------------------------------------------------------------------
# Name:        lists
# Purpose:
#
# Author:      Claire Joyce
#
# Created:     08/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

a=[1,3,5,7,11]
i=[13,17]
c=a+i
print c
i[0]=-1
d=[e+1 for e in a]
print d
d.append(i[0]+1)
d.append(i[-1]+1)
print d[-2]
