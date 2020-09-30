from math import *
import random

class Vec2d(object):
    x = 0
    y = 0
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
class Rect2d(object):
    v1 = None
    v2 = None
    def __init__(self,v1 = Vec2d(),v2 = Vec2d()):
        self.v1 = v1
        self.v2 = v2
class MotionRect(Rect2d):
    c = color(0)
    lastFrame = 0
    currentRadius = 10
    targetRadius = 30
    w = 10
    h = 10
    dir = 1
    depth = 0
    targetDepth = 0
    def __init__(self,v1,v2,c = color(0)):
        super(MotionRect,self).__init__(v1,v2)
        self.c = c
        self.w = self.getWidth()
        self.h = self.getHeight()
    def getWidth(self):
        return abs(self.v2.x - self.v1.x)
    def getHeight(self):
        return abs(self.v2.y - self.v1.y)
    def changeRadiusTo(self,targetRadius):
        if targetRadius < 0:targetRadius = 0
        if targetRadius > min(self.w,self.h) / 2.0:targetRadius = min(self.w,self.h) / 2.0
        self.targetRadius = targetRadius
    def update(self):
        if frameCount - self.lastFrame > 100:
            self.targetDepth = map(random.random(),0,1,-100,100)
            self.lastFrame = frameCount
            if random.random() < 0.5:
                self.dir = 1
            else:
                self.dir = -1
            endValue = map(self.dir,-1,1,0,min(self.w,self.h) / 2.0)
            self.changeRadiusTo(endValue)
        dr = self.targetRadius - self.currentRadius
        dd = self.targetDepth - self.depth
        if abs(dd) > 1:
            self.depth = self.depth + dd / 15
        if abs(dr) > 1:
            self.currentRadius = self.currentRadius + dr / 15.0
        else:self.currentRadius = self.targetRadius
    def display(self):
        self.update()
        push()
        translate(0,0,self.depth)
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

def divide(divider,level):
    if level < 1:
        return
    grid = []
    for i in range(4):
        dx = random.uniform(0.2,0.8)
        dy = random.uniform(0.2,0.8)
        dx = 0.5
        dy = 0.5
        if level > 1:
            nextType = 'full'
            if random.random() > 0.5:
                nextType = 'none'
            nextDivider = Divider(nextType,level - 1,dx,dy)
            divide(nextDivider,level - 1)
            grid.append(nextDivider)
        else:
            grid.append(Divider('none',level - 1))
    divider.children = grid
class RectManager(object):
    dividerGroup = []
    rectGroup = []
    root = None
    def __init__(self,root):
        self.root = root
    def addRect(self,subRect):
        self.rectGroup.append(subRect)
    def display(self):
        for r in self.rectGroup:
            r.display()
def getSubRectGroup(bRect,dv):
    v1 = bRect.v1
    v2 = bRect.v2
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
def createDivider(dRect,dv,m):
    if dv.type == 'none':
        m.addRect(dRect)
    elif dv.type == 'full':
        subRectGroup = getSubRectGroup(dRect,dv)
        for i in range(len(subRectGroup)):
            subRect = subRectGroup[i]
            subDivider = dv.children[i]
            createDivider(subRect,subDivider,m)

def setup():
    global basicRect,root,m1,basicRect2,root2,m2
    size(1000,1000,P3D)
    rectMode(CORNERS)
    dx = random.uniform(0.2,0.8)
    dy = random.uniform(0.2,0.8)
    dx = 0.5
    dy = 0.5
    root = Divider('full',2,dx,dy)
    divide(root,2)
    m1 = RectManager(root)
    basicRect = MotionRect(Vec2d(300,300),Vec2d(700,700))
    createDivider(basicRect,root,m1)
    
def draw():
    background(200)
    push()
    rotateX(0.2)
    rotateY(0.2)
    m1.display()
    pop()
