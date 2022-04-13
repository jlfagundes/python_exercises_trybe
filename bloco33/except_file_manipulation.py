try:
    arquivo = open("arquivo.txt", "r")
except OSError:
    # será executado caso haja uma exceção
    print("arquivo inexistente")
else:
    # será executado se tudo ocorrer bem no try
    print("arquivo manipulado e fechado com sucesso")
    arquivo.close()
finally: # Outra clausulo do conjunto try
    # será sempre executado, independentemente de erro
    print("Tentativa de abrir arquivo")
    