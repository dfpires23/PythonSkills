import math  # IMPORTA A BIBLIOTECA MATH PARA USAR FUNÇÕES MATEMÁTICAS

math.sqrt(16)  # RAIZ QUADRADA
math.pow(2, 3)  # POTÊNCIA (2 ELEVADO A 3)
math.floor(3.7)  # ARREDONDAR PARA BAIXO
math.ceil(3.3)  # ARREDONDAR PARA CIMA

# AS VARIÁVEIS DEVEM SER EXPLÍCITAS (snake_case)
# O código deve ser legível e fácil de entender, mesmo para quem não está familiarizado com a linguagem de programação.
# EXEMPLO DE CÓDIGOS MAUS
a = 10
b = 20
c = a + b
# EXEMPLO DE CÓDIGOS BONS
numero1 = 10
numero2 = 20
soma = numero1 + numero2
print(f"A soma de {numero1} e {numero2} é igual a {soma}.")

# ===

# COMPARAÇÕES
print(10 > 5)  # MAIOR QUE
print(10 < 5)  # MENOR QUE
print(10 >= 5)  # MAIOR OU IGUAL A
print(10 <= 5)  # MENOR OU IGUAL A
print(10 == 5)  # IGUAL A
print(10 != 5)  # DIFERENTE DE

# ===

# BOOLEANOS
verdadeiro = True
falso = False

idade = int(input("Introduz a tua idade: "))
maior_de_idade = idade >= 18
adolescente = (idade >= 12) & (idade < 18)
# adolescente = idade >= 12 and idade < 18  # O AND É USADO PARA VER SE AS DUAS CONDIÇÕES SÃO VERDADEIRAS, O & TAMBÉM FUNCIONA, MAS O AND É MAIS USADO EM PYTHON
# adolescente = 12 <= idade < 18  # TAMBÉM É POSSÍVEL USAR ESSA SINTAXE PARA VER SE A IDADE ESTÁ ENTRE 12 E 18

# USANDO O BOOLEANO PARA TOMAR DECISÕES
if maior_de_idade:  # SE A PESSOA FOR MAIOR DE IDADE
    print("És maior de idade.")
elif adolescente:  # SENÃO, SE A PESSOA FOR UM ADOLESCENTE
    print("És um adolescente.")
else:  # SENÃO, A PESSOA É UMA CRIANÇA
    print("És uma criança.")

# ===

# DEBUDDING
# O processo de encontrar e corrigir erros em um programa é chamado de debugging.
print(
    f"{idade=}, {maior_de_idade=}, {adolescente=}"
)  # IMPRIME O VALOR DAS VARIÁVEIS PARA VER SE ESTÃO CORRETAS

# ===

# EXERCÍCIO: REGISTAR UM PEDIDO DE COMIDA
print("""===========================
Bem-vindo ao nosso restaurante!
Temos os seguintes menus:
1. Menu 1: Arroz, Feijão e Bife
2. Menu 2: Macarrão, Frango e Legumes
===========================""")
registar_pedido = input("Quer fazer um pedido? (sim/não) ")

if registar_pedido == "sim":
    comida = int(input("Quer menu 1 ou menu 2? "))
    if comida == 1:
        print("Você escolheu menu 1.")
    elif comida == 2:
        print("Você escolheu menu 2.")
    else:
        print("Opção inválida.")
else:
    print("Pedido cancelado.")

# ===

# ATRIBUIÇÃO COM OPERADORES
soma = 0

soma = soma + 10  # SOMA RECEBE O VALOR DE SOMA MAIS 10
soma += 10

soma = soma - 5  # SUBTRAÇÃO
soma -= 5

soma = soma * 2  # MULTIPLICAÇÃO
soma *= 2

soma = soma / 2  # DIVISÃO
soma /= 2

# ===

# CICLOS DE REPETIÇÃO
# EXERCÍCIO: IMPRIMIR OS NÚMEROS DE 0 A 4
print("Números de 0 a 4:")
valor = 0
while valor < 5:  # ENQUANTO O VALOR FOR MENOR QUE 5
    print(f"{valor=}")
    valor += 1  # INCREMENTA O VALOR EM 1

# EXERCÍCIO: IMPRIMIR OS NÚMEROS DE 4 A 20
print("Números de 4 a 20:")
valor = 4
while valor <= 20:
    print(f"{valor=}")
    valor += 1

# EXERCÍCIO: IMPRIMIR OS NÚMEROS DE 10 A 2
print("Números de 10 a 2:")
valor = 10
while valor >= 2:
    print(f"{valor=}")
    valor -= 1  # DECREMENTA O VALOR EM 1

# EXERCÍCIO: IMPRIMIR OS NÚMEROS PARES DE 5 A 13
print("Números pares de 5 a 13:")
valor = 5
while valor <= 13:
    if valor % 2 == 0:
        print(f"{valor=}")
    valor += 1  # INCREMENTA O VALOR EM 1 PARA VER SE É PAR, MAS PODERIA SER INCREMENTADO EM 2 PARA IMPRIMIR APENAS OS NÚMEROS PARES

# valor = 6
# while valor <= 12:
#     print(f"{valor=}")
#     valor += 2 # INCREMENTA O VALOR EM 2 PARA IMPRIMIR APENAS OS NÚMEROS PARES

# EXERCÍCIO: IMPRIMIR OS NÚMEROS MULTIPLOS DE 9 DE 12 A 50
print("Números múltiplos de 9 de 12 a 50:")
valor = 12
while valor <= 50:
    if valor % 9 == 0:
        print(f"{valor=}")
    valor += 1  # INCREMENTA O VALOR EM 1 PARA VER SE É MÚLTIPLO DE 9, MAS PODERIA SER INCREMENTADO EM 9 PARA IMPRIMIR APENAS OS MÚLTIPLOS DE 9

# valor = 18
# while valor <= 45:
#     print(f"{valor=}")
#     valor += 9 # INCREMENTA O VALOR EM 9 PARA IMPRIMIR APENAS OS MÚLTIPLOS DE 9, MAS PODERIA SER INCREMENTADO EM 1 PARA VER SE É MÚLTIPLO DE 9

# EXERCÍCIO: SOMAR TODOS OS NÚMEROS DE 5 A 20
print("Soma dos números de 5 a 20:")
soma = 0
valor = 5
while valor <= 20:
    soma += valor
    valor += 1
print(f"{soma=}")

# EXERCÍCIO: MULTIPLICAR TODOS OS NÚMEROS DE 4 A 9
print("Multiplicação dos números de 4 a 9:")
produto = 1
valor = 4
while valor <= 9:
    produto *= valor
    valor += 1
print(f"{produto=}")

produto = 1
valor = 4
for valor in range(4, 10):  # O RANGE VAI ATÉ O NÚMERO ANTERIOR AO 10, OU SEJA, ATÉ O 9
    produto *= valor
print(f"{produto=}")

# EXERCÍCIO: IMPRIMIR AS PRESENÇAS DE UM ALUNO EM 11 DIAS
presencas = [
    "presente",
    "presente",
    "falta",
    "presente",
    "falta",
    "presente",
    "presente",
    "falta",
    "falta",
    "presente",
    "falta",
]

contador_faltas = 0
for assiduidade_do_dia in presencas:
    if assiduidade_do_dia == "falta":
        contador_faltas += 1
print(f"O aluno teve {contador_faltas} faltas.")
