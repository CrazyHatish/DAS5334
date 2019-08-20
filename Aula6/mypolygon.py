import turtle
from math import pi
bob = turtle.Turtle()

def square(t, length):
    for _ in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, n, length):
    for _ in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t, r):
    for _ in range(360):
        t.fd(2*pi*r/360)
        t.lt(1) 

def arc(t, angle, r):
    for _ in range(angle):
        t.fd(2*pi*r/360)
        t.lt(1) 


polygon(bob, 6, 30)
circle(bob, 100)
arc(bob, 90, 50)

turtle.mainloop()
