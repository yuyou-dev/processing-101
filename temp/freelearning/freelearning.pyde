from math import *
import random
class Vec2d(object):
    x = 0
    y = 0
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    def distance(self,v):
        dx = self.x - v.x
        dy = self.y - v.y
        return sqrt(dx * dx + dy * dy)
class Box2d(object):
    startVec = Vec2d(0,0)
    endVec = Vec2d(1,1)
    def __init__(self,v1 = Vec2d(0,0),v2 = Vec2d(1,1)):
        self.startVec = v1
        self.endVec = v2
class MotionPoint(object):
    x = 0
    y = 0
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    def display(self):
        point(x,y,z)
    def distance(self,p):
        return sqrt((p.x - self.x) * (p.x - self.x) + (p.y - self.y) * (p.y - self.y))
    
class MotionRect(object):
    center = MotionPoint()
    currentRadius = 10
    targetRadius = 30
    w = 10
    h = 10
    lastFrame = 0
    def __init__(self,center,w,h,d = 10):
        self.center = center
        self.w = w
        self.h = h
    def display(self):
        rect(self.center.x,self.center.y,self.w,self.h,self.currentRadius)
    def changeRadiusTo(self,targetRadius):
        if targetRadius < 0:targetRadius = 0
        if targetRadius > min(self.w,self.h) / 2.0:targetRadius = min(self.w,self.h) / 2.0
        self.targetRadius = targetRadius
    def update(self):
        if frameCount - self.lastFrame > (50 + random.randint(20,50)):
            self.lastFrame = frameCount
            self.changeRadiusTo(random.uniform(0,min(self.w,self.h) / 2.0))
        dr = self.targetRadius - self.currentRadius
        if abs(dr) > 1:
            self.currentRadius = self.currentRadius + dr / 10.0
        else:self.currentRadius = self.targetRadius

mr = None

    
def setup():
    size(400,400,P3D)
    fill(255,255,0)
    global mr
    
    center = MotionPoint(200,200)
    w = 100
    h = 100
    
    mr = MotionRect(center,w,h)
    
def draw():
    rectMode(CENTER)
    background(200)
    
    global mr
    mr.update()
    mr.display()

def mouseClicked():
    a = 3
