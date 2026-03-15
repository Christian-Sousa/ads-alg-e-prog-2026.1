import turtle
import math

def isosceles(t, r, angulo):
    base_angulo = (180 - angulo) / 2
    base = 2 * r * math.sin(math.radians(angulo) / 2)
    t.forward(r)
    t.left(180 - base_angulo)
    t.forward(base)
    t.left(180 - base_angulo)
    t.forward(r)
    t.left(180 + angulo)

def poligono(t, n, r):
    angulo = 360 / n
    for i in range(n):
        isosceles(t, r, angulo)

def move_turtle(t, distancia):
    t.penup()
    t.forward(distancia)
    t.pendown()
    
def main():
    bob = turtle.Turtle()
    bob.speed(3)

    poligono(bob, 5, 60)
    move_turtle(bob, 150)

    poligono(bob, 6, 60)
    bob.left(60)
    poligono(bob, 6, 60)
    move_turtle(bob, 150)

    poligono(bob, 7, 60)
    turtle.mainloop()

main()