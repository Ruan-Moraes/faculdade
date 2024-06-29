# Exemplo 01 - Estrutura de dados - Tuplas

# Tuplas são estruturas de dados imutáveis e estáticas
# São definidas por parênteses

mochila = ('Machado', 'Camisa', 'Bacon', 'Abacate')
print(mochila)

# Acessando elementos da tupla

print(mochila[0]) # Acessando o primeiro elemento
print(mochila[2]) # Acessando o terceiro elemento
print(mochila[0:2]) # Acessando do primeiro ao segundo elemento
print(mochila[2:]) # Acessando do terceiro elemento até o final
print(mochila[-1]) # Acessando o último elemento

for item in mochila:
    print('Na mochila tem: ', item)

# Tentando alterar um elemento da tupla

# mochila[0] = 'Faca' # Erro! Tuplas são imutáveis

# Exemplo 02 - Listas

# Listas são estruturas de dados mutáveis e dinâmicas
# São definidas por colchetes

mochila = ['Machado', 'Camisa', 'Bacon', 'Abacate']
print(mochila)

# Acessando elementos da lista

print(mochila[0]) # Acessando o primeiro elemento
print(mochila[2]) # Acessando o terceiro elemento
print(mochila[0:2]) # Acessando do primeiro ao segundo elemento
print(mochila[2:]) # Acessando do terceiro elemento até o final
print(mochila[-1]) # Acessando o último elemento

for item in mochila:
    print('Na mochila tem: ', item)

# Alterando um elemento da lista

mochila[0] = 'Faca'

print(mochila)

# Exemplo 03 - Strings tem comportamento de lista e tupla

# Strings são listas de caracteres

machado = 'Machado'
print(machado)

# Acessando elementos da string

print(machado[0]) # Acessando o primeiro elemento
print(machado[2]) # Acessando o terceiro elemento
print(machado[0:2]) # Acessando do primeiro ao segundo elemento
print(machado[2:]) # Acessando do terceiro elemento até o final
print(machado[-1]) # Acessando o último elemento

for letra in machado:
    print('Na palavra tem a letra: ', letra)

# Alterando um elemento da string

# machado[0] = 'F' # Erro! Strings são imutáveis

# Exemplo 04 - Dicionários

# Dicionários são estruturas de dados mutáveis e dinâmicas
# São definidas por chaves

mochila = {'Machado': 1, 'Camisa': 2, 'Bacon': 3, 'Abacate': 4}
print(mochila)

# Acessando elementos do dicionário

print(mochila['Machado']) # Acessando o valor associado à chave 'Machado'
print(mochila['Bacon']) # Acessando o valor associado à chave 'Bacon'

for item in mochila:
    print('Na mochila tem: ', item)

