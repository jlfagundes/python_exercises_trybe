#Teste para ver o erro ao abrir muitos arquivos ao
#Mesmo tempo e não fechar
arquivos = []
for index in range(10240):
    arquivos.append(open(f"arquivo{index}.txt", "w"))

# Retorno do Erro em tela abaixo:
#$ python3 many_files_open.py 
# Traceback (most recent call last):
#   File "C:\Users\jlfagundes\source\repos\python_study_trybe\python_exercises_trybe\bloco33\many_files_open.py", line 5, in <module>
# OSError: [Errno 24] Too many open files: 'arquivo8189.txt'