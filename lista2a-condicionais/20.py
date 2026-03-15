def ler_angulo(entrada):
    return int(input(entrada))

def determinar_quadrante(angulo):
    if 0<angulo<=90:
        return "1° quadrante"
    elif angulo>90 and angulo<=180:
        return "2° quadrante"
    elif angulo>180 and angulo<=270:
        return "3° quadrante"
    elif angulo>270 and angulo<=360: 
        return "4° quadrante"
    
def main():
    angulo = ler_angulo("Digita um ângulo qualquer ae chefe: ")
    print(f"O ângulo lido está situado no {determinar_quadrante(angulo)}")

main()