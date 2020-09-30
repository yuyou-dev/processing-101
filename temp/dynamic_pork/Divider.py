from math import *
import random
from Modules import *

class VisualDivider(object):
    children = []
    parent = []
    type = 'none'
    v = V3d()
    def __init__(self,parent):
        self.parent = parent
        self.type = 'none'
    def addChild(self,child):
        self.children.append(child)
    def divide(self):
        if random.random() < 0.5:
            self.type = 'full'
            x = map(random.random(),0,1,0.3,0.7)
            y = map(random.random(),0,1,0.3,0.7)
            z = map(random.random(),0,1,0.3,0.7)
            self.v = V3d(x,y,z)
            for i in range(8):
                child = VisualDivider(self)
                self.children.append(VisualDivider(self))
                if random.random() < 0.5:
                    child.divide()
        else:
            self.type = 'none'
            self.v = None
