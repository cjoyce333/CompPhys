"""
flock.py

This project simulates the motion of objects following a point, specifically like birds in a flocking movement.
"""

from visual import *
from random import randrange

class Flock:
    def __init__(self, num = 10, sidesize = 100.0):     

        display(title = "Flock")   
        
        self.NUMBIRDS = num             #the number of birds in the flock
        self.flock = []                 #empty list of birds
        self.RADIUS = 1                 #radius of bird
        self.SPACE = self.RADIUS * 5   #the space around each bird
        self.FACTOR = .95               #the amount of movement to the follow point
        self.NEGFACTOR = self.FACTOR * -1.0
        self.DT = 0.02                  #delay time
        self.SIDE = sidesize            #side of box
        self.MAXX = self.SIDE           #right
        self.MAXY = self.SIDE           #top
        self.MAXZ = self.SIDE           #front
        self.MINX = self.SIDE * -1.0    #left
        self.MINY = self.SIDE * -1.0    #bottom
        self.MINZ = self.SIDE * -1.0    #back
        self.Flock()                    

    def Flock(self):
        self.initPositions()      
        while (1==1):                   # it never stops
            rate(100)                   # animation speed, bigger = faster
            self.movebirds()  
            
    def initPositions(self):
        #wire frame of space
        rightBottom = curve(pos=[(self.MAXX, self.MINY, self.MINZ), (self.MAXX, self.MINY, self.MAXZ)], color=color.blue)
        rightTop = curve(pos=[(self.MAXX, self.MAXY, self.MINZ), (self.MAXX, self.MAXY, self.MAXZ)], color=color.blue)
        backLeft = curve(pos=[(self.MINX, self.MINY, self.MINZ), (self.MINX, self.MAXY, self.MINZ)], color=color.blue)
        backRight = curve(pos=[(self.MAXX, self.MINY, self.MINZ), (self.MAXX, self.MAXY, self.MINZ)], color=color.blue)
        frontLeft = curve(pos=[(self.MINX, self.MINY, self.MAXZ), (self.MINX, self.MAXY, self.MAXZ)], color=color.blue)
        frontRight = curve(pos=[(self.MAXX, self.MINY, self.MAXZ), (self.MAXX, self.MAXY, self.MAXZ)], color=color.blue)
        backBottom = curve(pos=[(self.MINX, self.MINY, self.MINZ), (self.MAXX, self.MINY, self.MINZ)], color=color.blue)
        backTop = curve(pos=[(self.MINX, self.MAXY, self.MINZ), (self.MAXX, self.MAXY, self.MINZ)], color=color.blue)
        frontBottom = curve(pos=[(self.MINX, self.MINY, self.MAXZ), (self.MAXX, self.MINY, self.MAXZ)], color=color.blue)
        frontTop = curve(pos=[(self.MINX, self.MAXY, self.MAXZ), (self.MAXX, self.MAXY, self.MAXZ)], color=color.blue)
        leftBottom = curve(pos=[(self.MINX, self.MINY, self.MINZ), (self.MINX, self.MINY, self.MAXZ)], color=color.blue)
        leftTop = curve(pos=[(self.MINX, self.MAXY, self.MINZ), (self.MINX, self.MAXY, self.MAXZ)], color=color.blue)
       
        # randomly place a bird
        for i in range(self.NUMBIRDS):         
            x = randrange(self.MINX, self.MAXX) #random left-right
            y = randrange(self.MINY, self.MAXY) #random up-down
            z = randrange(self.MINZ, self.MAXZ) #random front-back
            #colors
            r=randrange(1,4)
            if r==1:
                c=color.red
            if r==2:
                c=color.green
            if r==3:
                c=color.yellow
            if r==4:
                c=color.white
            #create a bird, add to flock list
            self.flock.append(sphere(pos=(x,y,z), radius=self.RADIUS, color=c))
        
    def movebirds(self):
        for i in range(self.NUMBIRDS):
            #manage birds flying off the edge
            if self.flock[i].x < self.MINX:
                self.flock[i].x = self.MAXX
                
            if self.flock[i].x > self.MAXX:
                self.flock[i].x = self.MINX
                
            if self.flock[i].y < self.MINY:
                self.flock[i].y = self.MAXY
                
            if self.flock[i].y > self.MAXY:
                self.flock[i].y = self.MINY
                
            if self.flock[i].z < self.MINZ:
                self.flock[i].z = self.MAXZ
                
            if self.flock[i].z > self.MAXZ:
                self.flock[i].z = self.MINZ

            v1 = vector(0.0,0.0,0.0)       
            v2 = vector(0.0,0.0,0.0)      
            v3 = vector(0.0,0.0,0.0)   
 
            v1 = self.follow(i)            
            v2 = self.avoid(i)          
            v3 = self.speed(i)
            
            Flockvelocity = vector(0.0,0.0,0.0)          
            Flockvelocity = Flockvelocity + v1 + v2 + v3
            
            self.flock[i].pos = self.flock[i].pos + (Flockvelocity*self.DT) #move bird

    def speed(self, aFlock):    # birds try to match speed of flock
        fvel = vector(0.0,0.0,0.0)  
            
        for i in range(self.NUMBIRDS):
            if i != aFlock:
                 fvel += self.flock[i].pos

        fvel /= (self.NUMBIRDS - 1.0)
        fvel /= (aFlock + 1)    #some of the birds are slower
        
        return fvel

    def follow(self, aFlock):    #birds fly to flock center
        fpoint = vector(0.0,0.0,0.0)                   
        for i in range(self.NUMBIRDS):              
            if i != aFlock:                          
                 fpoint += self.flock[i].pos  

        fpoint /= (self.NUMBIRDS - 1.0)     

        # move birds toward the center 
        if fpoint.x > self.flock[aFlock].x:
            fpoint.x = (fpoint.x - self.flock[aFlock].x)*self.FACTOR
        if fpoint.x < self.flock[aFlock].x:
            fpoint.x = (self.flock[aFlock].x - fpoint.x)*self.NEGFACTOR
        if fpoint.y > self.flock[aFlock].y:
            fpoint.y = (fpoint.y - self.flock[aFlock].y)*self.FACTOR
        if fpoint.y < self.flock[aFlock].y:
            fpoint.y = (self.flock[aFlock].y - fpoint.y)*self.NEGFACTOR
        if fpoint.z > self.flock[aFlock].z:
            fpoint.z = (fpoint.z - self.flock[aFlock].z)*self.FACTOR
        if fpoint.z < self.flock[aFlock].z:
            fpoint.z = (self.flock[aFlock].z - fpoint.z)*self.NEGFACTOR

        return fpoint 

    def avoid(self, aFlock):    # birds avoid other birds
        v = vector(0.0,0.0,0.0) 

        for i in range(self.NUMBIRDS):
            if i != aFlock:
                if abs(self.flock[i].x - self.flock[aFlock].x) < self.SPACE:
                    if self.flock[i].x > self.flock[aFlock].x:
                        v.x = self.SPACE * 12.0   
                    if self.flock[i].x < self.flock[aFlock].x:
                        v.x = -self.SPACE * 12.0
                if abs(self.flock[i].y - self.flock[aFlock].y) < self.SPACE:
                    if self.flock[i].y > self.flock[aFlock].y:
                        v.y = self.SPACE * 12.0
                    if self.flock[i].y < self.flock[aFlock].y:
                        v.y = -self.SPACE * 12.0
                if abs(self.flock[i].z - self.flock[aFlock].z) < self.SPACE:
                    if self.flock[i].z > self.flock[aFlock].z:
                        v.z = self.SPACE * 12.0
                    if self.flock[i].z < self.flock[aFlock].z:
                        v.z = -self.SPACE * 12.0

        return v

if __name__ == "__main__":
   
    i = Flock()     
