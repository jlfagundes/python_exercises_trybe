#importanto o modulo para trabalhar com json, não foi preciso instalar ja veio com python
import json

# O with abre o arquivo para trabalhar somente no contexto dele,
# sai do with automaticamente fecha o arquivo
with open("teste.json") as user_data:
    # print(user_data.read()) # read() para ler o arquivo json mais não transforma em dicionario python
    # print(json.load(user_data)) # json.load() le e transforma em dicionario python
    # print(json.load(user_data)[0]) # pegando o primeiro valor pelo indíce
    # print(json.load(user_data)[0]["name"]) # pegando o primeiro valor pelo indíce e pela chave
    
    userList = json.load(user_data) # Tras
    for user in userList:
        print(user["name"])