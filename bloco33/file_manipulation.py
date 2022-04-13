#Abre o arquivo com mode=w para poder escrever no arquivo
characteres_file = open("meus_personagens.txt", mode="w")

#Escrevendo no arquivo 
characteres_file.write("Lanterna Verde")
characteres_file.write("Homem Aranha")
characteres_file.write("Tio Patinhas")

print("Batman", file=characteres_file) #Print pode ser usado para imprimir no arquivo tbm

#Escrevendo lista no arquivo
more_characteres = ["Superman\n", "Flash\n"] #O \n é pra quebrar linha, senão escreve lado a lado

characteres_file.writelines(more_characteres)

#Fechar o arquivo
characteres_file.close
