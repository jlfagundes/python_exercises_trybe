print("O resultado é", 42)  # saída: O resultado é 42
print("Os resultado são", 6, 23, 42)  # saída: Os resultados são 6 23 42

#Usando o separador
print("Maria", "João", "Miguel", "Ana")  # saída: Maria João Miguel Ana
print("Maria", "João", "Miguel", "Ana", sep=", ")  # saída: Maria, João, Miguel, Ana

#Saída em duas linhas
print("Em duas ")
print("linhas.")

#Saída em uma linha usando o end=""
print("Na mesma", end="")
print("linha.")

#Modificando a saída padrão para erros
import sys #importa o modulo sys


err = "Arquivo não encontrado"
print(f"Erro aconteceu: {err}", file=sys.stderr) #Exemplo de literal string no python coloca o f antes

#Saída de casas decimais usando formatadores que vem depois dos :
x = 5
y = 3
print(f"{x} / {y} = {x / y:.2f}")  # saída: 5 / 2 = 1.67
# {x} é substituído por 5
# {y} é substituído por 3
# {x / y:.2f} O que vem após os dois pontos são formatadores, como nesse exemplo, duas casas decimais (.2f).
print(f"{x:.^3}")  # saída: ".5."
# . é o caractere utilizado para preencher
# ^ indica que o valor será centralizado
# 3 são o número de caracteres exibidos



