import turtle
from math import acos, degrees

bob = turtle.Turtle()

def is_triangle(t, a, b, c):
    if a == max(a, b, c) and b + c < a:
        print("No")
    elif b == max(a, b, c) and a + c < b:
        print("No")
    elif c == max(a, b, c) and a + b < c:
        print("No")
    else:
        draw_triangle(t, a, b, c)
        print("Yes")

def draw_triangle(t, a, b, c):
    angle_a = degrees(acos((b**2 + c**2 - a**2) / (2*b*c)))
    angle_b = degrees(acos((a**2 + c**2 - b**2) / (2*a*c)))
    angle_c = degrees(acos((a**2 + b**2 - c**2) / (2*a*b)))
    t.fd(c)
    t.lt(180 - angle_b)
    t.fd(a)
    t.lt(180 - angle_c)
    t.fd(b)
    t.lt(180 - angle_a)

a = input("Lado a: ")
b = input("Lado b: ")
c = input("Lado c: ")
is_triangle(bob, int(a), int(b), int(c))

turtle.mainloop()
