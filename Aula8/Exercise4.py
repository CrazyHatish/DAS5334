import turtle

def draw_koch(t, length):
    if length < 3:
        t.fd(length)
    else:
        draw_koch(t, length/3)
        t.lt(60)
        draw_koch(t, length/3)
        t.rt(120)
        draw_koch(t, length/3)
        t.lt(60)
        draw_koch(t, length/3)

def draw_snow(t, length):
    for _ in range(3):
        draw_koch(t, length)
        t.rt(120)

bob = turtle.Turtle()
    draw_snow(bob, 50)
