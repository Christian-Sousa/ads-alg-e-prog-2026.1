numero = int(input("Digite um número entre 0 e 100: "))

if numero < 0 or numero > 100:
    print("O número digitado está fora do intervalo de 0 a 100.")
else:
    if numero <= 1:
        eh_primo = False
    else:
        eh_primo = True
        
        # Testamos divisores de 2 até o número anterior a ele
        i = 2
        while i < numero:
            if numero % i == 0:
                eh_primo = False  # Se achou um divisor, não é primo
                # Não precisamos continuar testando se já descobrimos que não é primo
                i = numero
            else:
                i = i + 1

    if eh_primo:
        print(f"O número {numero} é primo.")
    else:
        print(f"O número {numero} não é primo.")