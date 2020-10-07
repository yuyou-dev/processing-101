add_library('sound')
from math import *
import random
from MotionRect import *

audio = None
amp = None
waveform = None
fft = None
samples = 200
sum = []
current = []
colors = []
barWidth = None
fBox = None

def setup():
    global audio,amp,waveform,samples,fft,sum,barWidth,colors,fBox
    
    size(1000,1000,P3D)
    smooth(8)
    global porkGroup,pork0
    r1 = 300
    r2 = 400
    x = width / 2
    y = height / 2
    aStart = 0
    aEnd = TAU / 4
    bStart = 0
    bEnd = TAU / 16

    file = SoundFile(this,'audio1.mp3')
    file.play()
    bands = 512
    fft = FFT(this, bands)
    fft.input(file);
    barWidth = width * 1.0/128;
    for i in range(128):
        colors.append(getColor())
        sum.append(0.0)
        current.append(0.0)
    fBox = FancyBox()
    fBox.create()
def getColor():
    colors = [color(13,127,190),color(245,10,10),color(251,228,20),color(255,255,255)]
    return colors[random.randint(0,3)]
def draw():
    print(millis())
    background(255)
    global amp,audio,waveform,samples,fft,sum,barWidth,colors,fBox
    
    fft.analyze()
    fill(color(13,127,190))
    push()
    
    strokeWeight(3)
    for i in range(128):
        sum[i] = 0.0
        sum[i] = sum[i] + (fft.spectrum[i] - sum[i]) * 0.2
        
        if current[i] > sum[i]:
            c = (current[i] - sum[i]) * 0.05
            current[i] = current[i] - c
        else:
            current[i] = sum[i]
            
    pop()
    push()
    translate(00,0)
    
    fBox.display(current)
    pop()