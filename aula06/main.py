# Exemplo 1 - Condicional Simples - if

x = int(input("Digite um valor inteiro: "))
y = int(input("Digite um segundo valor inteiro: "))

if (x > y):
    print("O primeiro valor é maior que o segundo!")

# Exemplo 2

if (x > y):
    print("O primeiro valor é maior que o segundo!")
if (y > x):
    print("O segundo valor é maior que o primeiro!")

# Exemplo 3 - Condicional Composta - if else

x = int(input("Digite um valor inteiro: "))
y = int(input("Digite um segundo valor inteiro: "))

if (x > y):
    print("O primeiro valor é maior que o segundo!")
else:
    print("O segundo valor é maior que o primeiro!")

# Exemplo 4

x = int(input("Digite um valor inteiro: "))

if (x % 2 == 0):
    print("O valor é par!")
else:
    print("O valor é ímpar!")

# Exemplo 5 - Condicional Aninhada - if else > if else

print("Escolha o que deseja comprar:")
print("1 - Maçã")
print("2 - Laranja")
print("3 - Banana")

produto = int(input("Digite o número do produto desejado: "))
quantidade = int(input("Digite a quantidade desejada: "))

if (produto == 1):
    valor = quantidade * 2.30
    print(f"Você comprou {quantidade} maçãs e o valor total é R$ {valor}")
else:
    if (produto == 2):
        valor = quantidade * 3.60
        print(f"Você comprou {quantidade} laranjas e o valor total é R$ {valor}")
    else:
        if (produto == 3):
            valor = quantidade * 1.85
            print(f"Você comprou {quantidade} bananas e o valor total é R$ {valor}")
        else:
            print("Produto inexistente!")

# Exemplo 6 - Condicional Encadeada - if elif else

print("Escolha o que deseja comprar:")
print("1 - Maçã")
print("2 - Laranja")
print("3 - Banana")

produto = int(input("Digite o número do produto desejado: "))
quantidade = int(input("Digite a quantidade desejada: "))

if (produto == 1):
    valor = quantidade * 2.30
    print(f"Você comprou {quantidade} maçãs e o valor total é R$ {valor}")
elif (produto == 2):
    valor = quantidade * 3.60
    print(f"Você comprou {quantidade} laranjas e o valor total é R$ {valor}")
elif (produto == 3):
    valor = quantidade * 1.85
    print(f"Você comprou {quantidade} bananas e o valor total é R$ {valor}")
else:
    print("Produto inexistente!")

# Exemplo 7

nome = input("Qual seu nome? ")
idade = int(input("Qual sua idade? "))

if (nome == 'Fulano'):
    print("Olá, Fulano!")
elif (idade < 18):
    print("Você não é o Fulano, e é menor de idade!")
elif (idade >= 200):
    print("Diferente de você, O Fulano não é imortal!")


# Exemplo 8 - Algebra Booleana

# - Não (not)

x = True
y = False

print(not x)
print(not y)

# - E (and)
x = False
y = True

print(x and y)

# - Ou (or)

x = True
y = False

print(x or y)

# Ṕrecedência de Operadores

# 1. Parênteses
# 2. Operadores aritméticos de potenciação ou raiz
# 3. Operadores aritméticos de multiplicação, divisão e resto (Módulo)
# 4. Operadores aritméticos de adição e subtração
# 5. Operadores relacionais
# 6. Operadores lógicos not
# 7. Operadores lógicos and
# 8. Operadores lógicos or
# 9. Atribuição

x = 10
y = 1

res = not x > y

print(res)

x = 10
y = 1
z = 5.5

res = (x > y) and (z == y) # True and False

print(res)

x = 10
y = 1
z = 5.5

res = x > y or not z == y  and y != y + z # True or not False and True > True or True and True > True or True > True

print(res)

# Exercício 3.3.1

m1 = float(input("Digite a nota da primeira matéria: "))
m2 = float(input("Digite a nota da segunda matéria: "))
m3 = float(input("Digite a nota da terceira matéria: "))

if (m1 >= 7 and m2 >= 7 and m3 >= 7):
    print("A maior nota é da primeira matéria!")
else:
    print("O aluno não passou de ano!")

