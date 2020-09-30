import math
import random

class VisualPoint(object):
    x = 0
    y = 0
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    def copy(self):
        return VisualPoint(self.x,self.y)

class VisualRect(object):
    startPoint = VisualPoint
    w = 0
    h = 0
    def __init__(self,startPoint,w,h):
        self.startPoint = startPoint
        self.w = w
        self.h = h
    def copy(self):
        sp = self.startPoint.copy()
        return VisualRect(sp,self.w,self.h)
    def display(self,c):
        fill(c)
        rect(self.startPoint.x,self.startPoint.y,self.w,self.h)
class Divider(object):
    type = 'none'
    left = 0.5
    top = 0.5
    c = color(0)
    children = []
    def __init__(self,type = 'none',left = 0.5,top = 0.5):
        self.type = type
        self.left = left
        self.top = top
        self.children = []
    def setValue(self,t,left = 0.5,top = 0.5):
        self.type = t
        self.left = left
        self.top = top
    def setColor(self,c):
        self.c = c
def getColor():
    colors = [
              color(13,127,190),
              color(245,10,10),
              color(251,228,20),
              color(255,255,255)
              ]
    return colors[random.randint(0,len(colors) - 1)]
def divideCross(p,vr,type,minSize,count,divider):
    rectGroup = []
    sp = vr.startPoint
    w = vr.w
    h = vr.h
    if count == 0:
        return
    if type == 'full':
        rect1 = VisualRect(sp.copy(),p.x - sp.x,p.y - sp.y)
        rect2 = VisualRect(p.copy(),w - (p.x - sp.x),h - (p.y - sp.y))
        rect3 = VisualRect(VisualPoint(p.x,sp.y),w - (p.x - sp.x),p.y - sp.y)
        rect4 = VisualRect(VisualPoint(sp.x,p.y),p.x - sp.x,h - (p.y - sp.y))
        rectGroup = [rect1,rect2,rect3,rect4]
    elif type == 'width':
        rect1 = VisualRect(sp.copy(),p - sp.x,vr.h)
        rect2 = VisualRect(VisualPoint(p,sp.y),w - (p - sp.x),h)
        rectGroup = [rect1,rect2]
    elif type == 'height':
        rect1 = VisualRect(sp.copy(),w,p - sp.y)
        rect2 = VisualRect(VisualPoint(sp.x,p),w,vr.h - (p - sp.y))
        rectGroup = [rect1,rect2]
    for r in rectGroup:
        sp = r.startPoint
        #r.display(getColor())
        nextRect = r.copy()
        left = random.uniform(0.2,0.8)
        top = random.uniform(0.2,0.8)
        x = map(left,0,1,sp.x,sp.x + w)
        y = map(top,0,1,sp.y,sp.y + h)
        if r.w > minSize and r.h > minSize:
            nextType = 'full'
            nextP = VisualPoint(x,y)
            dv = Divider(nextType,left,top)
            dv.setColor(getColor())
            divider.children.append(dv)
            divideCross(nextP,r,nextType,100,count - 1,dv)
        elif r.w > minSize and r.h <= minSize:
            nextType = 'width'
            nextP = x
            dv = Divider(nextType,left,top)
            dv.setColor(getColor())
            divider.children.append(dv)
            divideCross(nextP,r,nextType,100,count - 1,dv)
        elif r.w <= minSize and r.h > minSize:
            nextType = 'height'
            nextP = y
            dv = Divider(nextType,left,top)
            dv.setColor(getColor())
            divider.children.append(dv)
            divideCross(nextP,r,nextType,100,count - 1,dv)
        else:
            nextType = 'none'
            #return
root = None
firstRect = None
startTime = millis()
def mouseClicked():
    global root
    global firstRect
    x = map(mouseX,0,width,0,1)
    y = map(mouseY,0,height,0,1)
    root.setValue('full',x,y)
    reDraw(root,firstRect)

def reDraw(currentDivider,currentRect,dt = 0):
    global startTime
    vr = currentRect
    time = millis()
    radian = ((time + dt) % 2000) / 2000.0 * TAU
    t = currentDivider.type
    if t != 'none':
        currentRect.display(currentDivider.c)
    left = currentDivider.left  + 0.05 * sin(radian) * (1000.0 / time)
    top = currentDivider.top + 0.05 * cos(radian) * (1000.0 / time)
    sp = currentRect.startPoint
    w = currentRect.w
    h = currentRect.h
    children = currentDivider.children
    p = VisualPoint(map(left,0,1,sp.x,sp.x + w),map(top,0,1,sp.y,sp.y + h))
    if t == 'full':
        rect1 = VisualRect(sp.copy(),p.x - sp.x,p.y - sp.y)
        rect2 = VisualRect(p.copy(),w - (p.x - sp.x),h - (p.y - sp.y))
        rect3 = VisualRect(VisualPoint(p.x,sp.y),w - (p.x - sp.x),p.y - sp.y)
        rect4 = VisualRect(VisualPoint(sp.x,p.y),p.x - sp.x,h - (p.y - sp.y))
        rectGroup = [rect1,rect2,rect3,rect4]
    elif t == 'width':
        p = map(left,0,1,sp.x,sp.x + w)
        rect1 = VisualRect(sp.copy(),p - sp.x,vr.h)
        rect2 = VisualRect(VisualPoint(p,sp.y),w - (p - sp.x),h)
        rectGroup = [rect1,rect2]
    elif t == 'height':
        p = map(top,0,1,sp.y,sp.y + h)
        rect1 = VisualRect(sp.copy(),w,p - sp.y)
        rect2 = VisualRect(VisualPoint(sp.x,p),w,vr.h - (p - sp.y))
        rectGroup = [rect1,rect2]
    for i in range(len(children)):
        reDraw(children[i],rectGroup[i],dt + 600)
    return
def setup():
    size(1000,1000)
    strokeWeight(5)
    left = random.uniform(0.2,0.8)
    top = random.uniform(0.2,0.8)
    global root
    global firstRect
    root = Divider('full',left,top)
    start = VisualPoint(left * width,top * width)
    firstRect = VisualRect(VisualPoint(0,0),width,height)
    rectGroup = divideCross(start,firstRect,'full',100,4,root)
    reDraw(root,firstRect)
def draw():
    global root
    global firstRect
    x = map(mouseX,0,width,0,1)
    y = map(mouseY,0,height,0,1)
    root.setValue('full',x,y)
    reDraw(root,firstRect)
    
    return
