xp1 = int(input("Digite a abscissa do 1º ponto: "))
yp1 = int(input("Digite a ordenada do 1º ponto: "))
xp2 = int(input("Digite a abscissa do 2º ponto: "))
yp2 = int(input("Digite a ordenada do 2º ponto: "))
distancia = ((xp2 - xp1)**2 + (yp2 - yp1)**2)**0.5
print(f" > A distância entre os pontos ({xp1},{yp1}) e ({xp2,yp2}) é {distancia:.2f}.")