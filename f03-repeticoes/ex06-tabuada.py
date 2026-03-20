def main():
    for a in range(1, 11):
        print(f"Tabuada do {a}\n")
        for b in range(1, 11):
            print(f"{a} + {b} = {a + b}")
    
            print()

    for a in range(1, 11):
        print(f"Tabuada do {a}\n")
        for b in range(1, 11):
            print(f"{a} - {b} = {a - b}")
    
            print()
    
    for a in range(1, 11):
        print(f"Tabuada do {a}\n")
        for b in range(1, 11):
            print(f"{a} x {b} = {a * b}")
    
            print()

    for a in range(1, 11):
        print(f"Tabuada do {a}\n")
        for b in range(1, 11):
            print(f"{a} / {b} = {(a / b):.1f}")
    
            print()

main()