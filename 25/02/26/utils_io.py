def obter_nome(argumento):
    entrada = input(argumento)
    return entrada

def obter_numero_real(instrucoes):
    entrada = float(input(instrucoes))
    return entrada

def calcular_imc(altura, peso):
    imc = peso/(altura*altura)
    return imc

def classificar_imc(imc: float):
    if imc < 18.5:
        return "Abaixo do peso normal"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade grau I"
    elif imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"
    
def escrever(mensagem):
    printar = print(mensagem)
    return printar