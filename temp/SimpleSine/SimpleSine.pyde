add_library('sound')
from math import *
import random
sum = []
current = []
colors = [color(13,127,190),color(245,10,10),color(251,228,20),color(255,255,255)]
def normalDistribution(x):
    y = 1.0 / sqrt(TAU) * exp(- x * x / 2.0)
    return y

def setup():
    global sum,current,fft
    size(500,300,P3D)
    file = SoundFile(this,'music.mp3')
    file.play()
    smooth(8)
    fft = FFT(this, 512)
    fft.input(file);
    for i in range(128):
        sum.append(0.0)
        current.append(0.0)
        
def draw():
    global colors,fft,sum,current
    fft.analyze()
    for i in range(128):
        sum[i] = 0.0
        sum[i] = sum[i] + (fft.spectrum[i] - sum[i]) * 0.2
        
        if current[i] > sum[i]:
            c = (current[i] - sum[i]) * 0.1
            current[i] = current[i] - c
        else:
            current[i] = sum[i]
    background(255)
    stroke(0)
    strokeWeight(0.5)
    
        
    translate(0,height / 2.0)
    mil = millis()
    #mil = 0
    #noFill()
    for times in range(30):
        xRange = 1333
        r = 50
        
        dy = map(times,0,30,-99,99)
        dx = sqrt(100 * 100 - dy * dy)
        r = dx * 2.0
        scale = map(100 - abs(dy),0,100,0,1)
        dy = dy * 1.2

        v2 = normalDistribution(dy * 1.0 / r * 8.0) * 1
        v3 = map(sin(mil / (500.0 - times * 5)),-1,1,0,0.5)
        translate(0,0,5)
        timeScale = map(sin(millis() / (200.0 - times * 3)),-1,1,0,1)
        noStroke()
        fill(colors[int(noise(times) * 100) % 4])
        push()
        beginShape(QUAD_STRIP)
        for i in range(0,width,2):
            x = map(i,0,width,-xRange,xRange)
            v = normalDistribution(x * 1.0/ r) * map(r,0,100,0,100) * 10
            y = sin((i  + frameCount) / (8.0 + noise(times) * 4) + mil * noise(times + 0.1) * 5 / 850.0)
            y = y * v * scale * v2 * (noise(times + 0.01) + 0.5) * current[times] * 60 * timeScale * v3
            vertex(i,y + dy)
            vertex(i,height)
        endShape()
        pop()
        stroke(30)
        strokeWeight(1)
        noFill()
        beginShape()
        for i in range(0,width,2):
            x = map(i,0,width,-xRange,xRange)
            v = normalDistribution(x * 1.0/ r) * map(r,0,100,0,100) * 10
            y = sin((i + frameCount) / (8.0 + noise(times) * 4) + mil * noise(times + 0.1) * 5 / 850.0)
            y = y * v * scale * v2 * (noise(times + 0.01) + 0.5) * current[times] * 60 * timeScale * v3
            #vertex(i,height)
            vertex(i,y + dy)
        endShape()
