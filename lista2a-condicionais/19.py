def obter_numeros(argumento):
    return float(input(argumento))

def calcular_imc(peso, altura):
    imc = peso/(altura**2)
    return imc

def classificar_imc(imc):
    if imc < 25:
        return "ABAIXO DO PESO"
    elif 25>imc>30:
        return "PESO NORMAL"
    else:
        return "OBESIDADE MÓRBIDA"
    
def main():
    peso = obter_numeros("Peso: ")
    altura = obter_numeros("Altura: ")
    imc = calcular_imc(peso,altura)
    print(f"Com base nos valores lidos, você está {classificar_imc(imc)}")

main()
