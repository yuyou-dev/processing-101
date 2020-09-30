from math import *
import cv2
import random
from Modules import *
def setup():
    size(1000,1000)
    background(200)
    
    
    v1 = Vec2d(30,20)
    v2 = Vec2d(85,20)
    v3 = Vec2d(85,75)
    v4 = Vec2d(30,75)
    
    poly1 = Poly([v1,v2,v3,v4])
    
    poly1.display()
    
    r = 60
    v1 = Vec2d(30 + r,20 + r)
    v2 = Vec2d(85 + r,20 + r)
    v3 = Vec2d(85 + r,75 + r)
    v4 = Vec2d(30 + r,75 + r)
    
    poly2 = Poly([v1,v2,v3,v4])
    poly2.display()
    
    print(poly2.checkIntersect(poly1))
