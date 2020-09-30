from math import *
import random
from Modules import *
from Basic import *


class MotionRect(Rect2d):
    c = color(0)
    lastTime = 0
    currentRadius = 0
    targetRadius = 0
    w = 10
    h = 10
    dir = 1
    depth = 0
    targetDepth = 0
    count = 0
    number = 0
    def __init__(self,v1,v2,number):
        super(MotionRect,self).__init__(v1,v2)
        self.number = number
        self.c = self.getColor()
        self.w = self.getWidth()
        self.h = self.getHeight()
    def getWidth(self):
        return abs(self.v2.x - self.v1.x)
    def area(self):
        return self.getWidth() * self.getHeight()
    def getHeight(self):
        return abs(self.v2.y - self.v1.y)
    def setNumber(self,number):
        self.number = number
    def copy(self):
        return MotionRect(self.v1.copy(),self.v2.copy(),self.number)
    def changeRadiusTo(self,targetRadius):
        if targetRadius < 0:targetRadius = 0
        if targetRadius > min(self.w,self.h) / 2.0:targetRadius = min(self.w,self.h) / 2.0
        self.targetRadius = targetRadius
    def update(self,current):
        if millis() - self.lastTime > 3000:
            self.targetDepth = map(random.random(),0,1,0,400)
            self.count = self.count + 1
            #endValue = 0
            if random.random() < 0.5:
                self.dir = 1
            else:
                self.dir = -1
            if self.count == 5:
                self.count = 0
                endValue = 0
                self.targetDepth = 0
            else:
                endValue = map(self.dir,-1,1,0,min(self.w,self.h) / 2.0)
            self.lastTime = millis()
            self.changeRadiusTo(endValue)
        dr = self.targetRadius - self.currentRadius
        dd = self.targetDepth - self.depth
        if abs(dd) > 1:
            self.depth = self.depth + dd / 15
        if abs(dr) > 1:
            self.currentRadius = self.currentRadius + dr / 5.0
        else:self.currentRadius = self.targetRadius
    def getColor(self):
        colors = [
              color(13,127,190),
              color(245,10,10),
              color(251,228,20),
              color(255,255,255)
              ]
        return colors[random.randint(0,len(colors) - 1)]
    def display(self,current):
        self.update(current)
        push()
        #translate(0,0,self.depth)
        translate(0,0,map(current[self.number],0,0.03,0,600))
        fill(self.c,map(self.currentRadius,0,min(self.w,self.h) / 2.0,255,0))
        rect(self.v1.x,self.v1.y,self.v2.x,self.v2.y,self.currentRadius)
        pop()
class Divider(object):
    x = 0.5
    y = 0.5
    type = 'none'
    level = 0
    children = []
    def __init__(self,type = 'none',level = 0,x = 0.5,y = 0.5):
        self.type = type
        self.x = x
        self.y = y
        self.level = level
counter = 0
deck = []
for i in range(128):
    deck.append(i)
random.shuffle(deck)
class RectManager(object):
    rectGroup = []
    root = None
    def __init__(self,root):
        self.divide(root,3)
        self.root = root
        self.rectGroup = []
    def divide(self,divider,level):
        if level < 1:
            return
        grid = []
        for i in range(4):
            dx = 0.5
            dy = 0.5
            if level > 1:
                nextType = 'full'
                if random.random() > 0.3:nextType = 'none'
                nextDivider = Divider(nextType,level - 1,dx,dy)
                self.divide(nextDivider,level - 1)
                grid.append(nextDivider)
            else:
                grid.append(Divider('none',level - 1))
        divider.children = grid
        return
    def addRect(self,subRect):
        self.rectGroup.append(subRect.copy())
    def display(self,current):
        for r in self.rectGroup:
            r.display(current)
    def getSubRectGroup(self,bRect,dv):
        v1 = bRect.v1.copy()
        v2 = bRect.v2.copy()
        xRange = [v1.x,map(dv.x,0,1,v1.x,v2.x),v2.x]
        yRange = [v1.y,map(dv.y,0,1,v1.y,v2.y),v2.y]
        data = []
        for i in range(3):
            for j in range(3):
                if i < 2 and j < 2:
                    sv1 = Vec2d(xRange[i],yRange[j])
                    sv2 = Vec2d(xRange[i + 1],yRange[j + 1])
                    
                    global counter,deck
                    subRect = MotionRect(sv1,sv2,deck[counter])
                    counter = counter + 1
                    data.append(subRect)
        return data
    def createDivider(self,dRect,dv = None):
    
        if dv == None:dv = self.root
        if dv.type == 'none':
            
            self.addRect(dRect.copy())
            return
        elif dv.type == 'full':
            subRectGroup = self.getSubRectGroup(dRect.copy(),dv)
            for i in range(len(subRectGroup)):
                subRect = subRectGroup[i]
                subDivider = dv.children[i]
                self.createDivider(subRect,subDivider)
class FancyBox(object):
    faces = []
    def __init__(self):
        self.faces = []
    def create(self):
        minX = 400
        minY = 400
        maxX = 600
        maxY = 600
        m1 = RectManager(Divider('full',2,0.5,0.5))
        m1.createDivider(MotionRect(Vec2d(minX,minY),Vec2d(maxX,maxY),201))
        
        m2 = RectManager(Divider('full',2,0.5,0.5))
        m2.createDivider(MotionRect(Vec2d(minX,minY),Vec2d(maxX,maxY),202))
        
        m3 = RectManager(Divider('full',2,0.5,0.5))
        m3.createDivider(MotionRect(Vec2d(minX,minY),Vec2d(maxX,maxY),203))
    
        m4 = RectManager(Divider('full',2,0.5,0.5))
        m4.createDivider(MotionRect(Vec2d(minX,minY),Vec2d(maxX,maxY),204))
        
        m5 = RectManager(Divider('full',2,0.5,0.5))
        m5.createDivider(MotionRect(Vec2d(minX,minY),Vec2d(maxX,maxY),205))
        
        m6 = RectManager(Divider('full',2,0.5,0.5))
        m6.createDivider(MotionRect(Vec2d(minX,minY),Vec2d(maxX,maxY),206))
        self.faces = [m1,m2,m3,m4,m5,m6]
    def display(self,current):
        m1 = self.faces[0]
        m2 = self.faces[1]
        m3 = self.faces[2]
        m4 = self.faces[3]
        m5 = self.faces[4]
        m6 = self.faces[5]
        angle = millis() % 24000 / 24000.0 * TAU
        r = 100
        push()
        rectMode(CORNERS)
        strokeWeight(3)
        translate(500,500,-1000)
        rotateX(angle)
        rotateY(angle)
        fill(255,255,255,255)
        push()
        rotateX(angle * 10)
        rotateY(angle * 5)
        fill(map(sin(millis() / 12000.0 * TAU),-1,1,0,255),map(cos(millis()  / 12000.0 * TAU),-1,1,0,255),map(sin(millis()  / 12000.0 * TAU),-1,1,255,0))
        box(map(sin(millis()  / 10000.0 * TAU),-1,1,50,100))
        pop()
        push()
        translate(-width / 2,-width / 2,r)
        m1.display(current)
        pop()
        
        push()
        rotateX(TAU / 2)
        translate(-width / 2,-width / 2,r)
        m2.display(current)
        pop()
        push()
        rotateX(TAU / 2)
        rotateY(TAU / 4)
        translate(-width / 2,-width / 2,r)
        m3.display(current)
        pop()
        
        push()
        rotateX(TAU / 2)
        rotateY(TAU / 4 + TAU / 2)
        translate(-width / 2,-width / 2,r)
        m4.display(current)
        pop()
        
        push()
        rotateX(TAU / 4)
        translate(-width / 2,-width / 2,r)
        m5.display(current)
        pop()
        
        push()
        rotateX(TAU / 4 + TAU / 2)
        translate(-width / 2,-width / 2,r)
        m6.display(current)
        pop()
        
        pop()
