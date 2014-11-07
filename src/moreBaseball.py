#-------------------------------------------------------------------------------
# Name:        moreBaseball (4.4)
# Purpose:
#
# Author:      Claire
#
# Created:     09/10/2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from numpy import *
from math import *
from mpl_toolkits.mplot3d import *
import matplotlib.pyplot as plt

cy = 0
cz = 0

done = 0

def kD(v):      #define drag coefficient a la Giordano
    delta = 5.
    vd = 35.
    return 0.0039+0.0058/(1.+exp((v-vd)/delta))

def euler(vx,vy,vz):
    x=0
    y=0
    z=input("pitcher's release height:")
    t=0
    dt = 0.001
    kL=4.1E-4
    omega = 1800#spin of ball, rotation rate in rpm
    omega = omega*2.*pi/60. #converts spin to rad/s
    while x<= 18.44:
        X.append(x)
        Y.append(y)
        Z.append(z)

        v=sqrt(vx**2 + vy**2 + vz**2)

        ax = -kD(v)*v*vx + kL*omega*(vz*sin(phi)-vy*cos(phi))
        ay = -kD(v)*v*vy + kL*omega*vx*cos(phi)
        az = -kD(v)*v*vz - kL*omega*vx*sin(phi)-g

        vx += ax*dt
        vy += ay*dt
        vz += az*dt

        x+= vx*dt
        y+= vy*dt
        z+= vz*dt

while not done:
    X=[]
    Y=[]
    Z=[]

    TYPE = raw_input("Type of pitch (fastfball[f]/curveball[c]/slider[s]/screwball[w]: ").lower()

    if TYPE == "c":
        v=34.5  #pitch speed
        phi=45*pi/180. #spin direction

    elif TYPE == "s":
        v=37.5
        phi = 0.

    elif TYPE == "f":
        v=41.6
        phi=225*pi/180.

    elif TYPE == "w":
        v=34.5
        phi = 135*pi/180.

    else:
        v=42.
        phi=0.

    theta = 3.*pi/180. #set throwing angle 3 deg above horizontal
    vx=v*cos(theta)
    vy=0.
    vz=v*sin(theta)
    g=9.80665

    euler(vx,vy,vz)
    fig = plt.figure()
    Ax = Axes3D(fig)
    Ax.plot(X,Y,Z)
    Ax.set_xlim3d(0.,18.44)
    Ax.set_ylim3d(-1.,10.)
    Ax.set_zlim3d(0.,10.)
    Ax.plot_wireframe(array([[18.4,18.4],[18.4,18.4]]),
                    array([[-0.22,0.22],[-0.22,0.22]]),
                    array([[0.5,0.5],[1.1,1.1]]),
                    color = "r")
    cy =Y[len(Y)-1]-Y[0]
    cz =Z[len(Z)-1]-Z[0]


    plt.show()
    print TYPE,": ", cy," ",cz
    reply = raw_input("Again? y or n").lower()
    if reply == "n":
        done = 1

#f :  -0.231797184313   0.162539398516
#c :  0.282342528896   -0.856854044879
#s :  0.365557514645   -0.324090825981
#w :  -0.282342528896   -0.856854044879