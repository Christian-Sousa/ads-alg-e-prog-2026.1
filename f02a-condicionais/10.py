def obter_data():
    dia = int(input("Dia: "))
    mes = int(input("Mês: "))
    ano = int(input("Ano: "))
    return dia,mes,ano

def calcular():
    dia,mes,ano = obter_data()
    if 0<dia<=30 and 0<mes<=12 and ano>0:
        print("A data é válida.")
    else:
        print("A data não é válida.")
    return print()

def main():
    return calcular()

main()