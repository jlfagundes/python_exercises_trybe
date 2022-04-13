# escrita
file = open("arquivo.txt", mode="w") # Abre no mode escrite (write)
file.write("Trybe S2")
file.close()

# leitura
file = open("arquivo.txt", mode="r") # Abri no mode leitura (read)
content = file.read()
print(content)
file.close()  # não podemos esquecer de fechar o arquivo

# Fazendo a leitura de mais de uma linha por vez no laço for
# escrita
file = open("arquivo.txt", mode="w")
LINES = ["Olá\n", "mundo\n", "belo\n", "do\n", "Python\n"]
file.writelines(LINES)
file.close()

# leitura
file = open("arquivo.txt", mode="r")
for line in file:
    print(line)  # não esqueça que a quebra de linha também é um caractere da linha
file.close()  # não podemos esquecer de fechar o arquivo

# Leitura de arquivos em bytes
# escrita
file = open("arquivo.dat", mode="wb")
file.write(b"C\xc3\xa1ssio 30")  # o prefixo b em uma string indica que seu valor está codificado em bytes
file.close()

# leitura
file = open("arquivo.dat", mode="rb")
content = file.read()
print(content)  # saída: b'C\xc3\xa1ssio 30'
file.close()  # não podemos esquecer de fechar o arquivo