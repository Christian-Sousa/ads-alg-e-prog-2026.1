def obter_nome(nome):
    return input(nome)

def quantidade_horas():
    horas1 = int(input("Digite as horas trabalhadas do professor 1: "))
    total1 = horas1*float(input("Digite o valor por hora do professor 1: "))
    horas2 = int(input("Digite as horas trabalhadas do professor 2: "))
    total2 = horas2*float(input("Digite o valor por hora do professor 1: "))
    return total1, total2

def maior_total(total_p1,total_p2,p1,p2):
    if total_p1>total_p2:
        maior,p = total_p1,p1
    else:
        maior,p = total_p2,p2
    return maior,p

def main():
    nome_p1 = obter_nome("Nome do professor 1: ")
    nome_p2 = obter_nome("Nome do professor 2: ")
    total_p1, total_p2 = quantidade_horas()
    resultado_maior,nome_maior = maior_total(total_p1,total_p2,nome_p1,nome_p2)
    print(f"O professor {nome_p1} recebe R${total_p1} e o professor {nome_p2} recebe R${total_p2}.")
    print(f"O professor {nome_maior} recebe tem o salário maior de R${resultado_maior}.")

main()