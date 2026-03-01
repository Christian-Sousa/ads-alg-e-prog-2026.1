from utils_io import obter_numero_real, calcular_imc, classificar_imc, obter_nome, escrever

def main():
    nome = obter_nome("Nome: ")

    altura = obter_numero_real("Altura(em metros): ")
    peso = obter_numero_real("Peso(em Kg): ")

    imc = calcular_imc(altura, peso)

    classificacao = classificar_imc(imc)

    escrever(f"{nome}, seu IMC é {imc:.1f}({classificacao})")

main()