import turtle

def main():
    length = int(input("Digite o tamanho do lado do polígono: "))
    bob = turtle.Turtle()
    square(bob,length)

def square(t,length):
    for i in range(4):
        t.forward(length)
        t.left(90)
main()