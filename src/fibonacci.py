#-------------------------------------------------------------------------------
# Name:        fibonacci
# Purpose:
#
# Author:      Claire Joyce
#
# Created:     11/09/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

n=0
list = [0,1]
while n<3:
    n= input("Pick a number greater than 2 for the number of terms")

for i in range(0,n):
    new =list[len(list)-1] + list[len(list)-2]
    list.append(new)

print list