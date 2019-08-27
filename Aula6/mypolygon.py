import turtle
from math import pi, cos, sqrt, ceil
bob = turtle.Turtle()

def square(t, length):
    polygon(t, 4, length)

def polygon(t, n, length):
    polyline(t, n, 360, length)

def circle(t, r):
    arc(t, 360, r)

def arc(t, angle, r):
    circumference = 2 * pi * r
    n = ceil(circumference / 3)
    side_length = circumference / n
    polyline(t, n, angle, side_length) 

def polyline(t, n, angle, length):
    for _ in range(int(n*angle/360)):
        t.fd(length)
        t.lt(360/n)

def petal(t, angle, r):
    arc(t, angle, r)
    t.lt(180 - angle)
    arc(t, angle, r)

def flower(t, angle, petals, r):
    for i in range(petals):
        t.lt(i*360/petals)
        petal(t, angle, r)
        t.seth(0)

def draw_isoceles_triangle(t, base, angle):
    other_angle = 180 - angle*2
    sides = sqrt(base ** 2 / (2* (1-cos(other_angle*pi/180)) ))
    t.fd(base)
    t.lt(180 - angle)
    t.fd(sides)
    t.lt(180 - other_angle)
    t.fd(sides)
    t.lt(180 - angle)

def draw_triangle_poly(t, side, n):
    angle = ((n - 2) * 180 / n)
    for _ in range(n):
        draw_isoceles_triangle(t, side, angle/2)
        t.fd(side)
        t.lt(180 - angle)

def draw_spiral(t, length, loops):
    seg = loops*360
    for i in range(seg):
        t.fd(length/seg*((seg-i)/seg))
        t.lt(1)

#flower(bob, 75, 8, 150)

# draw_triangle_poly(bob, 50, 7)

draw_spiral(bob, 1000, 3)

turtle.mainloop()
