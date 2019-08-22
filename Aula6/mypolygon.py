import turtle
from math import pi, cos, sqrt
bob = turtle.Turtle()

def square(t, length):
    polygon(t, 4, length)

def polygon(t, n, length):
    polyline(t, n, 360, length)

def circle(t, r):
    arc(t, 360, r)

def arc(t, angle, r):
    circumference = 2 * pi * r
    n = int(circumference / 3)
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
    sides = sqrt(base ** 2 / (2*(1-cos(angle*pi/180))))
    t.fd(base)
    t.lt(180 - angle)
    t.fd(sides)
    t.lt(180 - 2*angle)
    t.fd(sides)

#flower(bob, 75, 8, 150)

draw_isoceles_triangle(bob, 100, 45)

turtle.mainloop()
