print("Olá, boa noite!")  # IMPRIMR
input("Está tudo bem? ")  # SCANNER

# ===

nome = "Daniel"  # ATRIBUIR VARIÁVEL
print("Olá, boa noite! " + nome)
# CONCATENAR STRING COM VARIÁVEL, PARA CONCATENAR É PRECISO USAR O +

# ===

# PEDIR AO UTILIZADOR PARA INTRODUZIR O NOME E GUARDAR NA VARIÁVEL NOME
nome = input("Introduz o teu nome: ")
print("Olá, boa noite! " + nome)

idade = input("Introduz a tua idade: ")
print("A tua idade é: " + idade + " anos.")

altura = input("Introduz a tua altura: ")
print("A tua altura é: " + altura + " metros.")

nacionalidade = input("Introduz a tua nacionalidade: ")
print("A tua nacionalidade é: " + nacionalidade)

# ===

nome = input("Introduz o teu nome: ")
print(f"Olá, boa noite! {nome}")
# O F STRING É USADO PARA USAR VARIÁVEIS DENTRO DA STRING DIRETO SEM PRECISAR DE CONCATENAR COM O +, É SÓ USAR AS CHAVES {} PARA USAR A VARIÁVEL DENTRO DA STRING

idade = input("Introduz a tua idade: ")
print(f"A tua idade é: {idade} anos.")

altura = input("Introduz a tua altura: ")
print(f"A tua altura é: {altura} metros.")

nacionalidade = input("Introduz a tua nacionalidade: ")
print(f"A tua nacionalidade é: {nacionalidade}")

# ===

print(f"""Olá, isto é o começo do meu livro.
      O meu nome é {nome} e eu tenho {idade} anos.
      Tenho {altura} metros e sou de {nacionalidade}.""")
# PARA USAR VÁRIAS LINHAS DE STRING, É SÓ USAR AS TRÊS ASPAS DUPLAS """ PARA ABRIR E FECHAR A STRING, E DENTRO DA STRING PODE USAR VARIÁVEIS COM O F STRING NORMALMENTE

# ===

a = input("Nr1: ")
b = input("Nr2: ")
print(type(a))  # PARA MOSTRAR O TIPO DA VARIÁVEL
print(type(b))
print(int(a) + int(b))  # É PRECISO FAZER CAST PARA CÁLCULAR

# CASTING
str(a)
float(a)
int(a)

# CÁLCULOS
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisao_inteira = a // b
resto = a % b
expoente = a**b

# ===

a = int(input("Nr1: "))
b = int(input("Nr2: "))
c = int(input("Nr3: "))
d = int(input("Nr4: "))
media = (a + b + c + d) / 4
print(f"A média é: {media}")

# ===
# AS VARIÁVEIS DEVEM SER EXPLÍCITAS (snake_case)

comprimento = int(input("Comprimento: "))  # SE TENTAR UM FLOAT, ELE DÁ ERRO !
largura = int(input("Largura: "))
area = comprimento * largura
print(f"A área é: {area}")

horas = int(input("Horas: "))
segundos = horas * 3600
print(f"O valor em segundos é: {segundos}")

graus_celsius = float(input("Celsius: "))
graus_fahrenheit = (graus_celsius * 9 / 5) + 32
print(f"O valor em Fahrenheit é: {graus_fahrenheit}")

# ===

UMA_HORA_EM_SEGUNDOS = 3600  # CONSTANTES DEVEM SER EM MAIÚSCULAS
# AS CONSTANTES SÃO VARIÁVEIS QUE NÃO DEVEM SER ALTERADAS, POR ISSO SÃO ESCRITAS EM MAIÚSCULAS PARA DIFERENCIAR DAS VARIÁVEIS NORMAIS
print(f"Uma hora tem {UMA_HORA_EM_SEGUNDOS} segundos.")
