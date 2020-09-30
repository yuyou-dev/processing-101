add_library('sound')
from math import *

sum = []
current = []
colors = [color(13,127,190),color(245,10,10),color(251,228,20),color(255,255,255)]
def setup():
    global sum,current,fft
    size(500,500,P3D)
    file = SoundFile(this,'music.mp3')
    file.play()
    bands = 512
    fft = FFT(this, bands)
    fft.input(file);
    for i in range(128):
        sum.append(0.0)
        current.append(0.0)
    
def draw():
    background(255)
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
            
    
    translate(0,height / 2.0 - 30)
    
    push()
    
    fill(255)
    #noStroke()
    smooth(8)
    for x in range(20):
        translate(0,0,5)
        push()
        fill(colors[x % 4])
        #fill(255)
        #noFill()
        #translate(0,0,map(x,0,20,-50,50))
        #strokeWeight(1)
        
        stroke(0)
        noStroke()
        beginShape(QUAD_STRIP)
        r = map(x,0,20,-10,10)
        r = abs(r)
        r = r *  2.0
        r = r * r / 10
        mil = millis()
        for i in range(0,width,5):
            t = map(i,0,width,-r,r)
            sy = 1.0 / sqrt(TAU) * exp(- t * t / 2.0) * 5
            sy = sy * 3
            y = sin((i + frameCount ) / (30.0 - x / 2.0)) * 100
            #scale = map(abs(i - 250),500,0,-1,1)
            scale = 1 * current[x] * 10
            timeScale = map(sin(mil / (200.0 - x * 3)),-1,1,0,1)
            y = y * scale * timeScale * sy + map(x,0,10,0,50)
            vertex(i,height)
            vertex(i,y)
        endShape()
        pop()
        
        push()
        fill(colors[x % 4])
        noFill()
        #translate(0,0,map(x,0,20,-50,50))
        strokeWeight(1)
        stroke(0)
        
        beginShape()
        r = map(x,0,20,-10,10)
        r = abs(r)
        r = r *  2.0
        r = r * r / 10
        for i in range(0,width,5):
            t = map(i,0,width,-r,r)
            sy = 1.0 / sqrt(TAU) * exp(- t * t / 2.0) * 5
            sy = sy * 3
            y = sin((i + frameCount ) / (30.0 - x / 2.0)) * 100
            #scale = map(abs(i - 250),500,0,-1,1)
            scale = 1 * current[x] * 10
            timeScale = map(sin(mil / (200.0 - x * 3)),-1,1,0,1)
            y = y * scale * timeScale * sy + map(x,0,10,0,50)
            vertex(i,y)
        endShape()
        pop()
    pop()
    
