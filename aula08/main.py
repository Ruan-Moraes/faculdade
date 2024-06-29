# Exemplo 1 - Sem função

print("|----------------|")
print("|      Menu      |")
print("|----------------|")


# Exemplo 2 - Com função

def realce():
    print("|" + "-" * 16 + "|")


realce()
print("|      Menu      |")
realce()


# Exemplo 3 - Com função e parâmetro

def realce(tamanho, caractere):
    print("|" + caractere * tamanho + "|")


realce(16, "~")
print("|      Menu      |")
realce(16, "~")


# Exemplo 4 - Com função e parâmetro padrão

def realce(tamanho=16, caractere="*"):
    print("|" + caractere * tamanho + "|")


realce()
print("|      Menu      |")
realce()


# Exercício 1

def borda(s1):
    tam = len(s1)

    if tam:
        print("+", "-" * tam, "+")
        print("|", s1, "|")
        print("+", "-" * tam, "+")


borda("Olá, mundo!")
borda("Python")
borda("Lógica de Programação")


# Exemplo 5 - Função com retorno

def soma(a, b):
    return a + b


print(soma(2, 3))


# Exemplo 5.1 - Função x Procedimento

# Função sempre retorna um valor

def soma(a, b):
    return a + b


# Procedimento não retorna valor

def imprime_soma(a, b):
    print(a + b)


# Exemplo 6 - Escopo de variáveis - Escopo Global

c = 0


def soma(a, b):
    global c

    c = a + b

    return c


print(soma(2, 3))
print(c)


# Exemplo 7 - Escopo de variáveis - Escopo Local

def soma(a, b):
    c = a + b

    return c


print(soma(2, 3))


# print(c) # Erro

# Exercício 2

def valida_string(pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)

    while (tam < min) or (tam > max):
        s1 = input(pergunta)
        tam = len(s1)

    return s1


print(valida_string("Digite uma string: ", 10, 20))

print('Você digitou uma string com o tamanho adequado!')

# Exemplo 8 - Exceção

# ZeroDivisionError
# TypeError
# ValueError
# IndexError

# while True
#     print('Olá, mundo!') - Erro de sintaxe

# print(100 * 1.0 / 0) - ZeroDivisionError

# while True:
#   try:
#       x = int(input('Digite um número: '))
#
#       break
#   except ValueError:
#       print('Digite um número válido!')

# Exemplo 9 - Função lambda

# def soma(a, b):
#     return a + b

soma = lambda a, b: a + b

print(soma(2, 3))