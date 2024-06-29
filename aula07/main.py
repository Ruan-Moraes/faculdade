# Exemplo 1 -  Sem estrutura de repetição

print(1)
print(2)
print(3)
print(4)
print(5)

x = 1
print(x)
x = x + 1
print(x)
x = x + 1
print(x)
x = x + 1
print(x)
x = x + 1
print(x)

# Exemplo 2 - Com estrutura de repetição - while

x = 1
while x <= 5:
    print(x)
    x = x + 1

# Exemplo 3 - while com problema - loop infinito

x = 1
while x <= 5:
    print(x)
    # x = x + 1

# Exercício 1 - Contadores

inicial = int(input('Digite o valor inicial: '))
final = int(input('Digite o valor final: '))

x = inicial
while x <= final:
    if (x % 2 == 0):
        print(x)
    x = x + 1

# Exercício 2 - Acumuladores

soma = 0
cont = 1

while cont <= 5:
    valor = int(input('Digite o valor: '))
    soma = soma + valor
    cont = cont + 1
media = soma / 5
print('A média dos valores é: ', media)

# Operadores especias de atribuição
# +=  | x = x + 1  - x += 1
# -=  | x = x - 1  - x -= 1
# *=  | x = x * 1  - x *= 1
# /=  | x = x / 1  - x /= 1
# %=  | x = x % 1  - x %= 1
# **= | x = x ** 1 - x **= 1
# //= | x = x // 1 - x //= 1

# Exercício 3

soma = 0
cont = 1

while cont <= 5:
    valor = int(input('Digite o valor: '))
    if valor % 2 == 0:
        soma += valor
    cont += 1

print('A soma dos valores pares é: ', soma)

# Exercício 4 - Validação de entrada

x = int("Digite um valor maior que 0: ")
while x <= 0:
    x = int("Digite um valor maior que 0: ")

print('Você digitou: ', x, 'Encerrando o programa...')

# Exemplo 4 - Break

print("Digite uma mensagem que irei repetir para você.")
print("Para sair digite 'sair'.")

while True:
    texto = input('')

    print(texto)

    if texto == 'sair':
        break

# Exemplo 5 - Continue

x = 0
while x < 10:
    x += 1
    if x % 2 == 0:
        continue
    print(x)

# Exemplo 6 - Thuthy e Falsy
# Falsy: 0, 0.0, '', "", [], (), {}, False, None
# Thuthy: Todos os demais

nome = ''

while not nome:
    nome = input('Digite seu nome: ')

print('Olá, ', nome)

# Exemplo 7 - For

for x in range(6):
    print(x)

for x in range(1, 6):
    print(x)

for x in range(1, 6, 2):
    print(x)

for x in range(5, 0, -1):
    print(x)

# Exercício 5 - Varredura de String

texto = input('Digite um texto: ')
for i in range(len(0, len(texto), 1)):
    print(texto[i])

# Exercício 6 - 1 a 100

soma = 0
qtd = 0

for x in range(1, 101):
    if (x % 2 == 0):
        soma += x
        qtd += 1

media = soma / qtd

print('A média dos valores pares é: ', media)

# Exemplo 8 - Estrutura de repetição aninhada

for x in range(1, 11):
    print('Tabuada do ', x)

    for y in range(1, 11):
        print(x, ' x ', y, ' = ', x * y)
