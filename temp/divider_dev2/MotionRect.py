from math import *
import random
class Vec2d(object):
    x = 0
    y = 0
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    def copy(self):
        return Vec2d(self.x,self.y)
class Rect2d(object):
    v1 = None
    v2 = None
    def __init__(self,v1 = Vec2d(),v2 = Vec2d()):
        self.v1 = v1
        self.v2 = v2
class MotionRect(Rect2d):
    c = color(0)
    lastFrame = 0
    currentRadius = 0
    targetRadius = 0
    w = 10
    h = 10
    dir = 1
    depth = 0
    targetDepth = 0
    count = 0
    def __init__(self,v1,v2,c = color(0)):
        super(MotionRect,self).__init__(v1,v2)
        self.c = self.getColor()
        self.w = self.getWidth()
        self.h = self.getHeight()
    def getWidth(self):
        return abs(self.v2.x - self.v1.x)
    def area(self):
        return self.getWidth() * self.getHeight()
    def getHeight(self):
        return abs(self.v2.y - self.v1.y)
    def copy(self):
        return MotionRect(self.v1.copy(),self.v2.copy(),self.c)
    def changeRadiusTo(self,targetRadius):
        if targetRadius < 0:targetRadius = 0
        if targetRadius > min(self.w,self.h) / 2.0:targetRadius = min(self.w,self.h) / 2.0
        self.targetRadius = targetRadius
    def update(self):
        if frameCount - self.lastFrame > 100:
            self.targetDepth = map(random.random(),0,1,0,1000)
            self.count = self.count + 1
            endValue = 0
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
            self.lastFrame = frameCount
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
    def display(self):
        self.update()
        push()
        translate(0,0,self.depth)
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
    def display(self):
        for r in self.rectGroup:
            r.display()
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
                    subRect = MotionRect(sv1,sv2)
                    
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
