import turtle

def main():
    length = int(input("Qual o tamanho do lado do polígono? "))
    n = int(input("Quantos lados tem o poligono? "))
    bob = turtle.Turtle()
    square(bob,length,n)

def square(bob,length,n):
    for i in range(n):
        bob.forward(length)
        bob.left(360/n)

main()
turtle.mainloop()