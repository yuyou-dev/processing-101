def setup():
    size(1000,1000,P3D)
    smooth(8)
def draw():
    background(200)
    angle = frameCount % 800 / 800.0 * TAU
    
    push()
    translate(width / 2,height / 2,0)
    rotateX(angle)
    rotateY(angle)
    box(500)
    pop()
