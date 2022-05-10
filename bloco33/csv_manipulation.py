#import o modulo csv
import csv

# Considera a "," como separador do CSV

with open("teste.csv") as user_data:
    user_list = csv.DictReader(user_data) # Ler o arquivo csv e armazena na variavel
    # print() de user_list sem tratar com for <csv.DictReader object at 0x00000271208AA410>
    
    for user in user_list:
        print(user["name"])


## Pode ser usado outra forma de ler
with open("teste.csv") as user_data:
    # Na expresssão abaixo é como desconstruir no javascript
    # a variavel "header" recebe a primeira linha
    # e o restante das linhas vai pra variavel "user_list"
    header, *user_list = csv.reader(user_data)
    print(header)
