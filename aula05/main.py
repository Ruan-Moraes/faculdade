print("Olá, mundo!")

print(3 + 2)

print("3" + "2")

print("Olá " + "mundo!")

# Operadores aritméticos

# +  | Adição
# -  | Subtração
# *  | Multiplicação
# /  | Divisão
# // | Divisão inteira
# %  | Resto da divisão
# ** | Potenciação

# Variáveis

nota = 8.5
disciplina = "Lógica de Programação"

print(nota)
print(disciplina)

# Nomeclarura de variáveis

# - Não pode começar com números
# - Não pode ter espaços
# - Não pode ter caracteres especiais
# - Pode conter underline
# - Pode conter números
# - Pode conter letras

# Exemplo de nome de variáveis

# nome_completo = "Fulano de Tal"
# idade = 30
# altura = 1.85
# peso = 80
# sexo = "M"

# Exemplo de nome de variáveis inválidos

# 1nome = "Fulano de Tal"
# nome completo = "Fulano de Tal"
# nome-completo = "Fulano de Tal"
# nome@completo = "Fulano de Tal"
# nomeCompleto = "Fulano de Tal" - Não é recomendado em Python

# Tipos de primeira de dados

# - int    | Números inteiros
# - float  | Números decimais
# - str    | Strings (texto)
# - bool   | Booleanos (True ou False)
# - list   | Listas
# - tuple  | Tuplas
# - dict   | Dicionários
# - set    | Conjuntos

# Juntar diferentes variáveis e strings

nome = "Fulano"
idade = 30

print("O nome é", nome, "e a idade é", idade)

# %s - String
# %d ou %i - Inteiro
# %f - Float

print("O nome é %s e a idade é %d" % (nome, idade))

# .format()

print("O nome é {} e a idade é {}".format(nome, idade))

# f-string

print(f"O nome é {nome} e a idade é {idade}")

# Tamanho (len)

nome = "Fulano de Tal"

print(len(nome))

# Função de entrada (input)

nome = input("Digite seu nome: ")
print("Olá, ", nome)
