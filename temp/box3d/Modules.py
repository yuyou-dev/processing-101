from math import *
import random

class Box3d(object):
    x = 0
    y = 0
    z = 0
    size = 20
    scale = 1.0
    c = None
    t = 255
    bright = 0.0
    def __init__(self,x,y,z,size):
        self.x,self.y,self.z,self.size = x,y,z,size
    def update(self,x,y,z,size):
        self.x,self.y,self.z,self.size = x,y,z,size
    def setColor(self,c):
        self.c = c
    def zoom(self,val):
        self.scale = val
    def display(self,c = color(255,255,255)):
        push()
        translate(self.x,self.y,self.z)
        c = self.c or c
        fill(c)
        box(self.size * self.scale)
        pop()
