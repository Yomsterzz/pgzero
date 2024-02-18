import pgzrun
import random

WIDTH = 500
HEIGHT = 500

def draw():
    r = 255
    g = 20
    b = random.randint(0,255)

    width = WIDTH
    height = HEIGHT - 200

    for i in range(1,20):
        mainrect = Rect((0,0), (width, height))
        mainrect.center = 250,270
        screen.draw.rect(mainrect, (r,g,b))
        width -= 20
        height += 20
        r -= 20
        g += 20



pgzrun.go()