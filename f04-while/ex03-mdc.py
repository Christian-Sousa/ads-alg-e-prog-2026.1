def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    a = num1
    b = num2

    while b != 0:
        if a < b:
            a, b = b, a
        resto = a % b
        a = b
        b = resto
    print(f"\nO MDC entre {num1} e {num2} é: {a}")

main()