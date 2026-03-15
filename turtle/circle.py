import turtle, math

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 100
    length = circumference / n
    polygon(t, n, length)

def polygon(t, n, length):
    for i in range(n):
        t.fd(length)
        t.lt(360 / n)

def main():
    bob = turtle.Turtle()
    circle(bob, 100)

main()