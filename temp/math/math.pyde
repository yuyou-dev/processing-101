from math import *
import random
from Modules import *
class Curve(object):
    points = []
    def __init__(self,points):
        self.points = points
    def addPoint(self,p):
        self.points.append(p)
        
class Bezier(object):
    p1 = None
    p2 = None
    c1 = None
    c2 = None
    def __init__(self,p1,c1,c2,p2):
        self.p1 = p1
        self.p2 = p2
        self.c1 = c1
        self.c2 = c2
    def getNextControlPoint(self):
        return Vec2d(self.p2.x * 2 - self.c2.x,self.p2.y * 2 - self.c2.y)
    def display(self):
        bezier(self.p1.x,self.p1.y,self.c1.x,self.c1.y,self.c2.x,self.c2.y,self.p2.x,self.p2.y)

class BezierPoint(Vec2d):
    next = None
    prev = None
    def __init__(self,x,y,prev):
        super(BezierPoint,self).__init__(x,y)
        self.prev = prev
        if(prev != None):prev.next = self
    def getPoint(self):
        return self.copy()
    def displayPoint(self):
        point(self.x,self.y)
        print(self.x,self.y)
    def displayLine(self):
        if self.next != None:
            line(self.x,self.y,self.next.x,self.next.y)
        else:return
def getSlice(points):
    s = beginShape()
    for p in points:
        s.vertex(p.x,p.y)
    s.endShape(CLOSE)
def mouseClicked():
    b = BezierPoint(mouseX,mouseY,None)
    b.displayPoint()
def setup():
    size(1000,1000,P3D)
    colorMode(HSB)
    smooth(8)
def draw():
    
    noFill()
    strokeWeight(1)
    stroke(0)
    
    p1 = Vec2d(85,20)
    c1 = Vec2d(10,10)
    p2 = Vec2d(15,80)
    c2 = Vec2d(30,30)
    
    b = Bezier(p1,c1,c2,p2)
    b.display()
    
    nextC1 = b.getNextControlPoint()
    nextP1 = p2.copy()
    nextC2 = Vec2d(135,135)
    nextP2 = Vec2d(140,70)
    
    nextB = Bezier(nextP1,nextC1,nextC2,nextP2)
    nextB.display()
    
    
    translate(100,100,0)
    bezier(85, 20, 10, 10, 90, 90, 15, 80)
    #bezier(15, 80, -90, -90, 100,200, 200,300)
    
    
    global lastFrame
    x = map(frameCount,0,100,0,TAU)
    y = map(sin(x),0,1,0,100)
    translate(500,500,0)
    stroke(map(frameCount % 240,0,240,0,360),360,360)
    line(frameCount,y,frameCount,0)
    

    #point(frameCount,y)
