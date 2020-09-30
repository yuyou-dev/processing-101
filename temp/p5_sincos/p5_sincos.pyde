def setup():
    size(710, 400, P3D);


def draw():
    background(250);
    noFill()
    rotateY(frameCount * 0.01)
    for j in range(5):
        push()
        for i in range(40):
            translate(
                sin(frameCount * 0.001 + j) * 100,
                sin(frameCount * 0.001 + j) * 100,
                i * 0.1
            )
            rotateZ(frameCount * 0.002)
            push()
            strokeWeight(0.2)
            sphere(8)
            pop()
        pop()
