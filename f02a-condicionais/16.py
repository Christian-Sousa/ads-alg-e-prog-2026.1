def obter_notas(notas):
    return float(input(notas))

def calcular_media(nota1,nota2):
    media = (nota1+nota2)/2
    if media >=7:
        return "APROVADO"
    else:
        exame = float(input("Nota do exame: "))
        media_final = (exame+media)/2
        if media_final>=7:
            return "APROVADO"
        else:
            return "REPROVADO"
        
def main():
    nota1 = obter_notas("Primeira nota: ")
    nota2 = obter_notas("segunda_nota: ")
    resultado = calcular_media(nota1, nota2)
    print(f"Você foi {resultado}.")

main()
