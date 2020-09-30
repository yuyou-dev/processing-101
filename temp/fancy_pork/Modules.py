from math import *
import random

class Vec3d(object):
    x = 0
    y = 0
    z = 0
    def __init__(self,x = 0,y = 0,z = 0):
        self.x = x
        self.y = y
        self.z = z
    def copy(self):
        return Vec3d(self.x,self.y,self.z)
    def display(self):
        point(self.x,self.y,self.z)
class Vec2d(object):
    x = 0
    y = 0
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
    def copy(self):
        return Vec2d(self.x,self.y)
    def add(self,x,y):
        self.x = self.x + x
        self.y = self.y + y
    def set(self,x,y):
        self.x = x
        self.y = y
    def distance(self,v):
        x1 = self.x
        y1 = self.y
        x2 = v.x
        y2 = v.y
        return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
class Line3d(object):
    p1 = Vec3d()
    p2 = Vec3d()
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    def copy(self):
        return Line3d(self.p1.copy(),self.p2.copy())
    def display(self):
        #strokeWeight(5)
        line(self.p1.x,self.p1.y,self.p1.z,self.p2.x,self.p2.y,self.p2.z)
class Line(object):
    p1 = Vec2d()
    p2 = Vec2d()
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    def copy(self):
        return Line(self.p1.copy(),self.p2.copy())
    def lerp(self,s):
        x = lerp(self.p1.x,self.p2.x,s)
        y = lerp(self.p1.y,self.p2.y,s)
        return Vec2d(x,y)
    def display(self):
        line(self.p1.x,self.p1.y,self.p2.x,self.p2.y)
class VisualPoint2d(Vec2d):
    next = None
    prev = None
    first = False
    parent = None
    def __init__(self,x,y):
        super(VisualPoint2d,self).__init__(x,y)
    def divide(self,s):
        next = self.next
        lNext = Line(self.copy(),self.next.copy())
        lPrev = Line(self.copy(),self.prev.copy())
        vNext = lNext.lerp(s)
        vPrev = lPrev.lerp(s)
        pNext = VisualPoint2d(vNext.x,vNext.y)
        pPrev = VisualPoint2d(vPrev.x,vPrev.y)
        if self.first == True:
            self.first = False
            pPrev.first = True
            pPrev.parent = self.parent
            self.parent.first = pPrev
        self.addNext(pNext)
        self.addPrev(pPrev)
        self.remove()
        if next.first != True:
            next.divide(s)
    def addNext(self,p):
        self.next.prev = p
        p.next = self.next
        self.next = p
        p.prev = self
    def addPrev(self,p):
        self.prev.next = p
        p.prev = self.prev
        p.next = self
        self.prev = p
    def remove(self):
        self.next.prev = self.prev
        self.prev.next = self.next
    def display(self):
        if self.next != None:
            x1 = self.x
            y1 = self.y
            x2 = self.next.x
            y2 = self.next.y
            line(x1,y1,x2,y2)
            if self.next.first != True:
                self.next.display()
class Polygon(object):
    first = Vec2d()
    def __init__(self,points):
        self.first = points[0]
        self.first.next = self.first
        self.first.prev = self.first
        self.first.first = True
        self.first.parent = self
        
        for i in range(1,len(points)):
            prev = points[i - 1]
            p = points[i]
            prev.addNext(p)
    def divide(self,s):
        self.first.divide(s)
    def display(self):
        self.first.display()

class SpherePoint(object):
    a = 0
    b = 0
    r = 0
    def __init__(self,r = 0,a = 0,b = 0):
        self.r = r
        self.a = a
        self.b = b
    def getPoint(self):
        a = self.a
        b = self.b
        r = self.r
        x = r * sin(a) * cos(b)
        y = r * cos(a) * cos(b)
        z = r * sin(b)
        return Vec3d(x,y,z)
    def getVec(self,sp):
        da = sp.a - self.a
        db = sp.b - self.b
        dr = sp.r - self.r
        x = dr * sin(da) * cos(db)
        y = dr * cos(da) * cos(db)
        z = dr * sin(db)
        return Vec3d(x,y,z)
    def getVecByRadius(self,r):
        da = self.a
        db = self.b
        dr = r - self.r
        x = dr * sin(da) * cos(db)
        y = dr * cos(da) * cos(db)
        z = dr * sin(db)
        return Vec3d(x,y,z)
class Pork(object):
    r1 = 0
    r2 = 0
    x = 0
    y = 0
    aStart = 0
    aEnd = 0
    bStart = 0
    bEnd = 0
    center = SpherePoint()
    dr = 0
    lastFrame = 0
    c = None
    def __init__(self,r1,r2,x,y,aStart,aEnd,bStart,bEnd):
        self.r1 = r1
        self.r2 = r2
        self.x = x
        self.y = y
        self.aStart = aStart
        self.bStart = bStart
        self.aEnd = aEnd
        self.bEnd = bEnd
        self.create()
        self.center = SpherePoint(r2,(aStart + aEnd) / 2,(bStart + bEnd) / 2)
        self.c = self.getColor()
    def update(self,r1,r2,x,y,aStart,aEnd,bStart,bEnd):
        self.r1 = r1
        self.r2 = r2
        self.x = x
        self.y = y
        self.aStart = aStart
        self.bStart = bStart
        self.aEnd = aEnd
        self.bEnd = bEnd
        self.create()
        self.center = SpherePoint(r2,(aStart + aEnd) / 2,(bStart + bEnd) / 2)
    def getSpherePoint(self,r,a,b):
        x = r * sin(a) * cos(b)
        y = r * cos(a) * cos(b)
        z = r * sin(b)
        return Vec3d(x,y,z)
    def create(self):
        aStart = self.aStart
        aEnd = self.aEnd
        bStart = self.bStart
        bEnd = self.bEnd
        r1 = self.r1
        r2 = self.r2
        x = self.x
        y = self.y
        
        rangeA = ceil(abs(aStart - aEnd) / TAU * 72)
        rangeB = ceil(abs(bStart - bEnd) / TAU * 2 * 36)
        
        aStep = int(rangeA)
        bStep = int(rangeB)
        g1 = []
        for j in range(0,bStep + 1):
            a = aStart
            bs = map(j,0,bStep,bStart,bEnd)
            p1 = self.getSpherePoint(r1,a,bs)
            p2 = self.getSpherePoint(r2,a,bs)
            g1.append(p1)
            g1.append(p2)

        g2 = []
        for j in range(0,bStep + 1):
            a = aEnd
            bs = map(j,0,bStep,bStart,bEnd)
            p1 = self.getSpherePoint(r1,a,bs)
            p2 = self.getSpherePoint(r2,a,bs)
            g2.append(p1)
            g2.append(p2)

        g3 = []
        for i in range(0,aStep + 1):
            b = bEnd
            aas = map(i,0,aStep,aStart,aEnd)
            p1 = self.getSpherePoint(r1,aas,b)
            p2 = self.getSpherePoint(r2,aas,b)
            g3.append(p1)
            g3.append(p2)

        g4 = []
        for i in range(0,aStep + 1):
            b = bStart
            aas = map(i,0,aStep,aStart,aEnd)
            p1 = self.getSpherePoint(r1,aas,b)
            p2 = self.getSpherePoint(r2,aas,b)
            g4.append(p1)
            g4.append(p2)
            
        g5 = []
        for i in range(1,aStep + 1):
            sg = []
            for j in range(0,bStep + 1):
                b = map(j,0,bStep,bStart,bEnd)
                aas = map(i,0,aStep,aStart,aEnd)
                aae = map(i - 1,0,aStep,aStart,aEnd)
                p1 = self.getSpherePoint(r2,aas,b)
                p2 = self.getSpherePoint(r2,aae,b)
                sg.append(p1)
                sg.append(p2)
            g5.append(sg)

        g6 = []
        for i in range(1,aStep + 1):
            sg = []
            for j in range(0,bStep + 1):
                b = map(j,0,bStep,bStart,bEnd)
                aas = map(i,0,aStep,aStart,aEnd)
                aae = map(i - 1,0,aStep,aStart,aEnd)
                p1 = self.getSpherePoint(r1,aas,b)
                p2 = self.getSpherePoint(r1,aae,b)
                sg.append(p1)
                sg.append(p2)
            g6.append(sg)
        
        
        lines = []
        for j in range(0,bStep):
            a = aStart
            bs = map(j,0,bStep,bStart,bEnd)
            p1 = self.getSpherePoint(r1,a,bs)
            p2 = self.getSpherePoint(r2,a,bs)
            bsn = map(j + 1,0,bStep,bStart,bEnd)
            p1n = self.getSpherePoint(r1,a,bsn)
            p2n = self.getSpherePoint(r2,a,bsn)
            
            lines.append(Line3d(p1,p1n))
            lines.append(Line3d(p2,p2n))
            if j == bStep - 1:
                c = 5
                lines.append(Line3d(p1n,p2n))
        for j in range(0,bStep):
            a = aEnd
            bs = map(j,0,bStep,bStart,bEnd)
            bsn =map(j + 1,0,bStep,bStart,bEnd) 
            p1 = self.getSpherePoint(r1,a,bs)
            p2 = self.getSpherePoint(r2,a,bs)
            p1n = self.getSpherePoint(r1,a,bsn)
            p2n = self.getSpherePoint(r2,a,bsn)
            
            lines.append(Line3d(p1,p1n))
            lines.append(Line3d(p2,p2n))
            if j == 0:
                lines.append(Line3d(p1,p2))
        for i in range(0,aStep):
            b = bEnd
            aas = map(i,0,aStep,aStart,aEnd)
            p1 = self.getSpherePoint(r1,aas,b)
            p2 = self.getSpherePoint(r2,aas,b)
            
            asn = map(i + 1,0,aStep,aStart,aEnd)
            
            p1n = self.getSpherePoint(r1,asn,b)
            p2n = self.getSpherePoint(r2,asn,b)
            lines.append(Line3d(p1,p1n))
            lines.append(Line3d(p2,p2n))
            
            if i == aStep - 1:
                c = 5
                lines.append(Line3d(p1n,p2n))
        for i in range(0,aStep):
            b = bStart
            aas = map(i,0,aStep,aStart,aEnd)
            p1 = self.getSpherePoint(r1,aas,b)
            p2 = self.getSpherePoint(r2,aas,b)
            
            asn = map(i + 1,0,aStep,aStart,aEnd)
            
            p1n = self.getSpherePoint(r1,asn,b)
            p2n = self.getSpherePoint(r2,asn,b)
            lines.append(Line3d(p1,p1n))
            lines.append(Line3d(p2,p2n))
            if i == 0:
                c = 5
                lines.append(Line3d(p1,p2))
        self.data = [g1,g2,g3,g4,g5,g6,lines]
    def getColor(self):
        colors = [color(13,127,190),color(245,10,10),color(251,228,20),color(255,255,255)]
        return colors[random.randint(0,3)]
    def display(self,type):
        c = self.c
        statusRange = frameCount % 400
        va = sin(frameCount % 100 / 100.0 * TAU)
        if statusRange < 175 or statusRange >= 375:
            fill(c,map(va,-1,1,255,0))
            v = map(va,-1,1,self.center.r,self.center.r * 3)
        else:
            fill(c)
            v = map(va,-1,1,self.center.r,self.center.r)
        if type == '1':
            fill(c)
        if type == '2':
            noFill()
        if type == '3':
            a = 10
        pos = self.center.getVecByRadius(v)
        #translate(pos.x,pos.y,pos.z)

        g1 = self.data[0]
        g2 = self.data[1]
        g3 = self.data[2]
        g4 = self.data[3]
        g5 = self.data[4]
        g6 = self.data[5]
        g7 = self.data[6]

        #noFill()
        strokeWeight(1)
        stroke(0,0,0,40)
        
        if type == '3':
            a = 5
        else:
            noStroke()
        beginShape(QUAD_STRIP)
        for p in g1:
            vertex(p.x,p.y,p.z)
        endShape()
    
        beginShape(QUAD_STRIP)
        for p in g2:
            vertex(p.x,p.y,p.z)
        endShape()
        
        beginShape(QUAD_STRIP)
        for p in g3:
            vertex(p.x,p.y,p.z)
        endShape()
        beginShape(QUAD_STRIP)
        for p in g4:
            vertex(p.x,p.y,p.z)
        endShape()   
            
        for sg in g5:
            beginShape(QUAD_STRIP)
            for p in sg:
                vertex(p.x,p.y,p.z)
            endShape()
        for sg in g6:
            beginShape(QUAD_STRIP)
            for p in sg:
                vertex(p.x,p.y,p.z)
            endShape()
        x = self.x
        y = self.y
        #translate(x,y)
        #translate(pos.x,pos.y,pos.z)
        stroke(0)
        strokeWeight(2)      
        for l in g7:
            l.display()
  
        
        
    
