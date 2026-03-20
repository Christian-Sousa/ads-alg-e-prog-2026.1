def ler_num(entrada):
    return float(input(entrada))

def main():
    n = ler_num("Número decimal: ")
    print(f"Número arredondado: {n:.0f}")  

main()