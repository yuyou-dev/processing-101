from math import *
import random
from Modules import *
colors = [
    [13,127,190],
    [245,10,10],
    [251,228,20],
    [255,255,255]
    ]
boxes = []
def brighten(x,y,z,val):
    global boxes
    box = boxes[x][y][z]
    box.bright = box.bright + val
    
    group = boxes[x - 2:x + 2][x - 1:y + 2][z - 1:z + 2]
    print(len(group))
    for yBox in group:
        for zBox in yBox:
            for item in zBox:
                x = 5
def updateBox(x,y,z):
    global boxes
    box = boxes[x][y][z]
def setup():
    size(600,600,P3D)
    smooth(8)
    global boxes
    for x in range(-100,101,40):
        yBox = []
        for y in range(-100,101,40):
            zBox = []
            for z in range(-100,101,40):
                box = Box3d(x,y,z,35)
                zBox.append(box)
            yBox.append(zBox)
        boxes.append(yBox)
    brighten(1,2,2,2)
def draw():
    background(255)
    strokeWeight(1)
    camera(0,0,(height / 2.0) / tan(PI * 30.0 / 180.0),0,0,0,0,1,0)
    rotateX(millis() / 2000.0)
    rotateY(millis() / 2000.0)
    global boxes,colors
    i = 0
    randX = noise(millis() / 1000.0) * 6
    randY = noise(millis() / 8999.0) * 6
    randZ = noise(millis() / 7998.0) * 6
    for x in range(6):
        for y in range(6):
            for z in range(6):
                ax = (x - randX) * (x - randX)
                ay = (y - randY) * (y - randY)
                az = (z - randZ) * (z - randZ)
                distance = sqrt(ax + ay + az)
                r = abs(sin(millis() / 1200.0) * 4)
                t = map(distance,0,r,255,100)
                size = map(distance,0,6,10,30)
                if t < 0:
                    t = 0
                if t > 255:
                    t = 255
                boxes[x][y][z].t = t
                boxes[x][y][z].size = size
    for x in range(len(boxes)):
        yBox = boxes[x]
        for y in range(len(yBox)):
            zBox = yBox[y]
            for z in range(len(zBox)):
                box = zBox[z]
                r = noise(x,y,z +  + millis() / 2105.0) * 255
                g = noise(x + millis() / 1000.0,y + 0.1,z + 0.1) * 255
                b = noise(x + 0.2,y  + millis() / 1300.0,z + 0.2) * 255
                t = box.t
                
                num = x + y * 6 + z * 36
                
                col = colors[num % 4]
                r = col[0]
                g = col[1]
                b = col[2]
                
                c = color(r,g,b,t)
                
                box.display(c)
