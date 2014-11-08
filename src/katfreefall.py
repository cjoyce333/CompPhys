#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      KatherineMJB
#
# Created:     02/10/2014
# Copyright:   (c) KatherineMJB 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from matplotlib import pyplot as plt

#yo = input("Enter initial height")
#vo = input("Enter initial velocity")
g = 9.81
#tv = input("Enter the terminal velocity")

def euler(y, vy, vt ):
    t = 0
    dt = .01
    plt.xlabel("TIme (s)")
    plt.ylabel("Height(m)")
    while(y>=0):
        plt.plot(t,y,'ro')
        ay = -t*(1+vy/vt)
        vy = vy + ay*dt
        y = y + vy*dt
        t = t+dt

done = 0

while not done:
    y = input("height, initial")
    vy = input("velocity, initial")
    tv = input("terminal velocity")
    euler(y, vy, tv)
    plt.show()
    reply = raw_input("Run again? y or n")
    if(reply == 'n'):
        done = 1
        print ("DONE")
