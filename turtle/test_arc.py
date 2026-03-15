import turtle, math

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 10
    length = circumference / n
    polygon(t, n, length)
    polygon2(t, n, length)

def polygon(t, n, length):
    arco = int(n/4)
    for i in range(arco):
        t.forward(length)
        t.left(360 / n)

def polygon2(t, n, length):
    t.left(180-(2*360/n))
    arco = int(n/4)
    for i in range(arco):
        t.forward(length)
        t.left(360 / n)

'''
def polygon_verse(t, n, length):
    arco = int(n/2)
    for i in range(arco):
        t.forward(length)
        t.right(360 / n)
'''

def main():
    bob = turtle.Turtle()
    bob.speed(3)
    circle(bob, 100)
    turtle.mainloop()
main()