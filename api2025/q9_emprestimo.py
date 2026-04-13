import os

def main():
    os.system('cls')

    renda_mensal=float(input('insira o valor da sua renda mensal: R$'))

    emprestimo=float(input('Insira o valor do empréstimo: R$'))
    while emprestimo<1518.0:
        print('O valor mínimo de empréstimo é de R$1518,00')
        emprestimo=float(input('Insira o valor do empréstimo: R$'))

    quant_parcelas=int(input('Insira a quantidade de parcelas do empréstimo: '))
    while 2>quant_parcelas or quant_parcelas>24:
        print('DESCULPE! É PERMITIDO APENAS EMPRÉSTIMOS EM NO MÍNIMO x2 E NO MÁXIMO x24.')
        quant_parcelas=int(input('Insira a quantidade de parcelas do empréstimo: '))

        
    if quant_parcelas<=6:
        selic = (14.75/100)*(50/100)
    elif quant_parcelas<=12:
        selic = (14.75/100)*(75/100)
    elif quant_parcelas<=18:
        selic = 14.75/100
    else:
        selic = (14.75/100)*(130/100)

    valor_parcela=float(emprestimo/quant_parcelas)
    iof = (0.38/100)*emprestimo + (0.0082/100)/(quant_parcelas*30)
    juros_sem_selic = emprestimo+iof
    juros_total=selic+juros_sem_selic+quant_parcelas
    montante=emprestimo+juros_total
    valor_parcela_total=montante/quant_parcelas


    if valor_parcela<=((30/100)*renda_mensal):
        print(f'\n> IOF: R${iof:.2f}')
        print(f'> Juros: R${juros_total:.2f}')
        print(f'> Total a pagar: R${montante:.2f}')
        print(f'> Parcela mensal: x{quant_parcelas} de R${valor_parcela_total:.2f}')
        print('\n> Empréstimo APROVADO.\n')
    else:
        print(f'\n> IOF: R${iof:.2f}')
        print(f'> Juros: R${juros_total:.2f}')
        print(f'> Total a pagar: R${montante:.2f}')
        print(f'> Parcela mensal: x{quant_parcelas} de R${valor_parcela_total:.2f}')
        print('\n> Empréstimo NEGADO.\n')

main()
