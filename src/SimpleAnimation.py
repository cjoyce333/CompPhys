'''
Created on Oct 14, 2014

@author: Claire Joyce
'''

from matplotlib.pylab import *
import time
from matplotlib.pyplot import draw

ion() # turns off interaction mode

x = arange(0,2*pi, 0.01)
line, = plot(x,x) #initial plot does nothing 
line.axes.set_ylim(-3,3)

starttime = time.time()
t=0

while t<10.0:
    t=time.time()-starttime
    y=-2*sin(x)*sin(t)
    
    line.set_ydata(y) #update plot data
    draw    #redraw