numerador_fracao1 = int(input("numerador da 1º fração: "))
denominador_fracao1 = int(input("denominador da 1º fração: "))
numerador_fracao2 = int(input("numerador da 2º fração: "))
denominador_fracao2 = int(input("denominador da 2º fração: "))
denominador_total = denominador_fracao1*denominador_fracao2
numerador_total = denominador_total/denominador_fracao1*numerador_fracao1 + denominador_total/denominador_fracao2*numerador_fracao2
print(f" > {numerador_fracao1}/{denominador_fracao1} + {numerador_fracao2}/{denominador_fracao2} = {numerador_total}/{denominador_total}")