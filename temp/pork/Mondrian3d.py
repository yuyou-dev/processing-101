from math import *
import random
from Modules import *

class VisualPoint(Vec3d):
    def __init__(self,x,y,z):
        super(VisualPoint,self).__init__(x,y,z)
    def copy(self):
        return VisualPoint(self.x,self.y,self.z)
    def distance(self,v):
        return sqrt((self.x - v.x) * (self.x - v.x) +(self.y - v.y) * (self.y - v.y) +(self.z - v.z) * (self.z - v.z))
    def mult(self,value):
        self.x = self.x * value
        self.y = self.y * value
        self.z = self.z * value
        

class VisualBox(object):
    startPoint = None
    endPoint = None
    distanceX = 0
    distanceY = 0
    distanceZ = 0
    divider = None
    pork = None
    def __init__(self,startPoint,endPoint):
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.distanceX = abs(endPoint.x - startPoint.x)
        self.distanceY = abs(endPoint.y - startPoint.y)
        self.distanceZ = abs(endPoint.z - startPoint.z)
    def copy(self):
        return VisualBox(self.startPoint.copy(),self.endPoint.copy())
    def updateMatrix(self):
        self.distanceX = abs(self.endPoint.x - self.startPoint.x)
        self.distanceY = abs(self.endPoint.y - self.startPoint.y)
        self.distanceZ = abs(self.endPoint.z - self.startPoint.z)
    def getCenter(self):
        return VisualPoint((self.endPoint.x + self.startPoint.x) / 2,(self.endPoint.y + self.startPoint.y) / 2,(self.endPoint.z + self.startPoint.z) / 2)
    def addDivider(self,divider):
        self.divider = divider
    def getPoint(self):
        px = map(self.divider.v3d.x,0,1,self.startPoint.x,self.endPoint.x)
        py = map(self.divider.v3d.y,0,1,self.startPoint.y,self.endPoint.y)
        pz = map(self.divider.v3d.z,0,1,self.startPoint.z,self.endPoint.z)
        return VisualPoint(px,py,pz)
    def createPork(self):
        r1 = self.startPoint.z
        r2 = self.endPoint.z
        x1 = self.startPoint.x
        x2 = self.endPoint.x
        y1 = self.startPoint.y
        y2 = self.endPoint.y
        r1 = map(r1,-200,200,0,300)
        r2 = map(r2,-200,200,0,300)
        aStart = map(x1,-200,200,-TAU / 4,TAU / 4)
        aEnd = map(x2,-200,200,- TAU / 4,TAU / 4)
        bStart = map(y1,-200,200,0,TAU)
        bEnd = map(y2,-200,200,0,TAU)
        self.pork = Pork(r1,r2,0,0,aStart,aEnd,bStart,bEnd)
    def display(self,c):
        push()
        fill(c)
        strokeWeight(1)
        self.pork.display(c)
        pop()
        return

class Divider(object):
    type = 'none'
    v3d = None
    box3d = None
    children = []
    c = color(0)
    maxBox = None
    showBox = None
    def __init__(self,type = 'none',box3d = None,maxBox = None,parent = None):
        x = map(random.random(),0,1,0.3,0.7)
        y = map(random.random(),0,1,0.3,0.7)
        z = map(random.random(),0,1,0.3,0.7)
        self.v3d = VisualPoint(x,y,z)
        self.type = type
        self.box3d = box3d
        self.box3d.addDivider(self)
        self.children = []
        self.c = self.getColor()
        self.maxBox = maxBox
    def getColor(self):
        colors = [color(13,127,190),color(245,10,10),color(251,228,20),color(255,255,255)]
        return colors[random.randint(0,3)]
    def setColor(self,c):
        self.c = c
    def display(self):
        if self.type == 'none':
            self.forceDisplay()
            return True
        return False
    def createShowBox(self):
        maxBox = self.maxBox
        startPoint = VisualPoint(
            map(self.box3d.startPoint.x,0,1,maxBox.startPoint.x,maxBox.endPoint.x),
            map(self.box3d.startPoint.y,0,1,maxBox.startPoint.y,maxBox.endPoint.y),
            map(self.box3d.startPoint.z,0,1,maxBox.startPoint.z,maxBox.endPoint.z)
        )
        endPoint = VisualPoint(
            map(self.box3d.endPoint.x,0,1,maxBox.startPoint.x,maxBox.endPoint.x),
            map(self.box3d.endPoint.y,0,1,maxBox.startPoint.y,maxBox.endPoint.y),
            map(self.box3d.endPoint.z,0,1,maxBox.startPoint.z,maxBox.endPoint.z)
        )
        self.showBox = VisualBox(startPoint,endPoint) 
        self.showBox.createPork()
    def forceDisplay(self):
        self.showBox.display(self.c)
    def displayAll(self):
        if self.display():
            return
        for child in self.children:
            child.displayAll()
    def divideNext(self):
        maxBox = self.maxBox
        v1 = self.box3d.startPoint
        v2 = self.box3d.getPoint()
        v3 = self.box3d.endPoint
        distance = v1.distance(v3)
        if distance < 0.9:
            return
        group = [
            [v1.x,v2.x,v3.x],
            [v1.y,v2.y,v3.y],
            [v1.z,v2.z,v3.z]
        ]
        data = []
        for i in range(3):
            l1data = []
            for j in range(3):
                l2data = []
                for k in range(3):
                    x = group[0][i]
                    y = group[1][j]
                    z = group[2][k]
                    point = VisualPoint(x,y,z)
                    l2data.append(point)
                l1data.append(l2data)
            data.append(l1data)
        if self.type == 'full':
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        startPoint = data[i][j][k].copy()
                        endPoint = data[i + 1][j + 1][k + 1].copy()
                        subBox = VisualBox(startPoint,endPoint)
                        if random.random() < 0.5:
                            subDivider = Divider('full',subBox,maxBox,self)
                            self.children.append(subDivider)
                            subDivider.divideNext()
                        else:
                            subDivider = Divider('none',subBox,maxBox,self)
                            subDivider.createShowBox()
                            self.children.append(subDivider)
                                 
    
