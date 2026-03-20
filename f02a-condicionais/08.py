def data_atual():
    dia = int(input("Dia atual: "))
    mes = int(input("Mês atual: "))
    ano = int(input("Ano atual: "))
    return dia,mes,ano

def data_nascimento():
    dia = int(input("Dia da data de nascimento: "))
    mes = int(input("Mês da data de nascimento: "))
    ano = int(input("Ano da data de nascimento: "))
    return dia,mes,ano

def calcular():
    dia_a,mes_a,ano_a=data_atual()
    total_a=dia_a+mes_a*30+ano_a*365
    dia_n,mes_n,ano_n=data_nascimento()
    total_n=dia_n+mes_n*30+ano_n*365
    total = total_a-total_n
    total_ano = total//365
    total_mes = (total%365)//30
    total_dia = (total%365)%30
    if total_mes==0 and total_dia == 0:
        resultado = print(f"Sua idade: {total_ano} anos, {total_mes} meses, {total_dia} e dias.\nFELIZ ANIVERSARIO!!!")
    else:
        resultado = print(f"Sua idade: {total_ano} anos, {total_mes} meses, {total_dia} e dias.")
    return resultado

def main():
    resultado = calcular()
    return resultado

main()