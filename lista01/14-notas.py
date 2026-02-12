nota1 = float(input("Digite a 1ª nota: "))
peso_nota1 = float(input("Digite o peso da 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
peso_nota2 = float(input("Digite o peso da 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))
peso_nota3 = float(input("Digite o peso da 3ª nota: "))
calculo = (nota1*peso_nota1 + nota2*peso_nota2 + nota3*peso_nota3)/peso_nota1+peso_nota2+peso_nota3
print(f"média ponderada igual a {calculo}")