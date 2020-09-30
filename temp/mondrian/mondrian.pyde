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

class VisualLine(object):
    p1 = VisualPoint()
    p2 = VisualPoint()
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

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

padding = 40;
def getColor():
    colors = [
              color(13,127,190),
              color(245,10,10),
              color(251,228,20),
              color(255,255,255)
              ]
    return colors[random.randint(0,len(colors) - 1)]
def divideCross(p,vr,type='full',minSize = 100,count = 0):
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
        fill(getColor())
        #fill(255,random.randint(100,150),random.randint(0,150))
        rect(sp.x,sp.y,r.w,r.h)
        nextRect = r.copy()
        if r.w > minSize and r.h > minSize:
            nextType = 'full'
            x = sp.x + random.randint(padding,r.w - padding)
            y = sp.y + random.randint(padding,r.h - padding)
            nextP = VisualPoint(x,y)
            count = count - 1
            divideCross(nextP,nextRect,nextType,100,count)
        elif r.w > minSize and r.h <= minSize:
            nextType = 'width'
            nextP = random.randint(sp.x + padding,sp.x + r.w - padding)
            divideCross(nextP,nextRect,nextType,100)
        elif r.w <= minSize and r.h > minSize:
            nextType = 'height'
            nextP = random.randint(sp.y + padding,sp.y + r.h - padding)
            divideCross(nextP,nextRect,nextType,100)
        else:
            nextType = 'none'
            #return

def drawCross(p,vr):
    x = p.x
    y = p.y
    strokeWeight(5)
    line(vr.startPoint.x,p.y,vr.startPoint.x + vr.w,p.y)
    line(vr.startPoint.x + p.x,vr.startPoint.y,vr.startPoint.x + p.x,vr.startPoint.y + vr.h)
    return
def mousePressed():
    println(1)
    background(255,255,255)
    start = VisualPoint(mouseX,mouseY)
    currentRect = VisualRect(VisualPoint(0,0),width,height)
    rectGroup = divideCross(start,currentRect,'full',100,5);
def setup():
    size(1000,1000)
    strokeWeight(5)
    start = VisualPoint(random.randint(100,width - 100),random.randint(100,height - 100))
    currentRect = VisualRect(VisualPoint(0,0),width,height)
    rectGroup = divideCross(start,currentRect,'full',100,5);
def draw():
    return
    start = VisualPoint(mouseX,mouseY)
    currentRect = VisualRect(VisualPoint(0,0),width,height)
    rectGroup = divideCross(start,currentRect,'full',100,5);
    return

    
