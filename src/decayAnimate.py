#-------------------------------------------------------------------------------
# Name:        decayanimate
# Purpose:
#
# Author:      Claire
#
# Created:     14/10/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

# def function to generate plot
def data_gen():
    t=data_gen.t
    cnt = 0
    while cnt<1000:
        cnt+= 1
        t+= 0.05
        yield t, np.sin(2*np.pi*t)*np.exp(-t/10)

data_gen.t = 0
fig, ax = plt.subplots()
line, =ax.plot([],[], lw=2)
ax.set_ylim(-1.1, 1.1)
ax.set_xlim(0,5)
ax.grid()

xdata,ydata=[],[]

def run(data):
    t, y=data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax.get_xlim()
    if t>xmax:
        ax.set_xlim(xmin,2*xmax)
        ax.figure.canvas,plt.draw
    line.set_data(xdata,ydata)
    return line,

anime = ani.FuncAnimation(fig, run, data_gen, blit = True, interval=10,repeat=False)
plt.show()


