import turtle
import math

def isosceles(t, r, angle):
    base_angle = (180 - angle) / 2
    base = 2 * r * math.sin(math.radians(angle) / 2)
    t.forward(r)
    t.left(180 - base_angle)
    t.forward(base)
    t.left(180 - base_angle)
    t.forward(r)
    t.left(180)

def pie(t, n, r):
    angle = 360 / n
    for i in range(n):
        isosceles(t, r, angle)
        t.left(angle)

def move_turtle(t, distance):
    t.penup()
    t.forward(distance)
    t.pendown()
    
bob = turtle.Turtle()
bob.speed(1)

pie(bob, 5, 60)
move_turtle(bob, 150)

pie(bob, 6, 60)
bob.left(60)

pie(bob, 6, 60)
move_turtle(bob, 150)

pie(bob, 7, 60)
turtle.mainloop()