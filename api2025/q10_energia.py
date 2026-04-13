import os

def main():
    os.system('cls')

    consumidores = int(input('Insira a quantidade de faturas que deseja calcular: '))
    for i in range(consumidores+1):
        kwh = 0.89
        nome = input('Nome do consumidor: ')
        consumo = int(input('Consumo(KWh): '))
        if consumo<=30:
            kwh = 0
            iluminacao = 0
        else:
            iluminacao = kwh*3/100
            
        if consumo>200:
            kwh = kwh + kwh*30/100
        
        fatura=kwh*consumo
        icms = fatura*25/100
        pis = fatura*3.75/100
        total=fatura+icms+pis

        print(f'''
            ***TALÃO MENSAL XPTO***
            Consumidor: {nome}
            Consumo(KWh): {consumo}
            Consumo(R$): R${fatura:.2f}(valor por KWh: R${kwh:.2f})
            Bandeira Tarifária: R$ XXXX (valor por 100KWh: R$ XXXX)
            Total sem Impostos: R${fatura:.2f}
            ICMS: R${icms:.2f}
            PIS/COFINS: R${pis:.2f}
            Iluminação Pública: R${iluminacao:.2f}

--------------------------------------------------------------------------
            Total a Pagar: R${total:.2f}
''')

main()
        