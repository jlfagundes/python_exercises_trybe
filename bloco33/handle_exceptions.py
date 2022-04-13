from ast import Break


while True: # Enquanto for verdadeiro
    try:
        x = int(input("Digite um valor, por favor: "))
        break
    except ValueError:
        print("Ops! O numero não é válido... tente novamente")
