import sys #Importa o modulo sys

if __name__ == "__main__": #função if
    for argument in sys.argv: #função for
        print("Received => ", argument)


# Para executar digite no terminal << python3 arquivo.py 2 4 "teste" >>
# A saída será:
# Received ->  arquivo.py
# Received ->  2
# Received ->  4
# Received ->  teste
