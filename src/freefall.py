#-------------------------------------------------------------------------------
# Name:        freefall (4.1)
# Purpose:
#
# Author:      Clarissa Joyce
#
# Created:     02/10/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from matplotlib import pyplot as plt
g=9.81
xx=[]
yy=[]
def euler(y,vy,vt):
    t=0
    dt=0.01
    plt.xlabel("Time, s")
    plt.ylabel("Height, m")

    while y>=0:
        plt.plot(t,y,"bo")
        xx.append(t)
        yy.append(y)
        #ay = -g*(1+vy/vt) #stokes acceleration
        ay = -g*(1+vy*abs(vy)/(vt*vt)) #Newton's law of drag
        vy += ay*dt
        y+= vy*dt
        t+= dt
done = 0

while not done:
    y,vy = input("initial height, velocity")
    vt=input("terminal velocity")
    euler(y,vy,vt)
    turnIdx = yy.index(max(yy))
    print "The max height is ",max(yy)
    print "Ascent time: ",xx[turnIdx]
    print "Descent time: ",(xx[len(xx)-1]-xx[turnIdx+1])
    plt.show()
    reply = raw_input("Again? y or n")
    if reply == 'n':
        done = 1
        print "Fin"


