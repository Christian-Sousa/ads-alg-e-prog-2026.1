def main():
    genero = input('M(Masculino) / F(Feminino): ').strip().upper()

    while genero=='M'or genero=='F':
        nota = float(input('Insira a nota do aluno: '))
        notas_geral=[]
        notas_masculino=[]
        notas_feminino=[]
        notas_geral.append(nota)
        if genero=='M':
            notas_masculino.append(nota)
            quant_masculino=len(notas_masculino)
            media_masculino=sum(notas_masculino)/len(notas_masculino)
        elif genero=='F':
            notas_feminino.append(nota)
            quant_feminino=len(notas_feminino)
            media_feminino=sum(notas_feminino)/len(notas_feminino)
        quant_alunos=len(notas_geral)
        maior_nota_geral=max(notas_geral)
        menor_nota_geral=min(notas_geral)
        media_geral=sum(notas_geral)/len(notas_geral)

        genero = input('M(Masculino) / F(Feminino): ').strip().upper()
    
    def verificar_desempenho(n):
        if 0<=n<=2:
            return 'PÉSSIMO'
        elif n>2 and n<=4:
            return 'RUIM'
        elif n>4 and n<=7:
            return 'REGULAR'
        elif n>7 and n<=8:
            return 'BOM'
        else:
            return('EXCELENTE')

    print(f'Quantidade de homens: {quant_masculino}')
    print(f'Quantidade de mulheres: {quant_feminino}')
    print(f'\nTotal de aluno: {quant_alunos}')
    print(f'Maior nota: {maior_nota_geral}')
    print(f'Menor nota: {menor_nota_geral}')
    print(f'Média das notas: {media_geral}')
    print(f'Desempenho dos homens: {verificar_desempenho(media_masculino)}')
    print(f'Desempenho das mulheres: {verificar_desempenho(media_feminino)}')
    print(f'Desempenho da turma: {verificar_desempenho(media_geral)}')

main()