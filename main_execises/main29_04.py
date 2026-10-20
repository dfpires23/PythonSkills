# NEGAÇÃO
verdade = True
falso = not verdade  # A NEGAÇÃO DE VERDADEIRO É FALSO
print(f"{verdade=}, {falso=}")

valor = 0
print(f"{valor > 5=}, {not valor > 5=}")

while valor < 5:
    valor += 1
    if valor == 3:
        print(f"ups, {valor=}")
        continue  # O CONTINUE VAI PULAR O RESTO DO CÓDIGO E VOLTAR PARA O INÍCIO DO CICLO
    print(f"{valor=}")

while valor < 5:
    valor += 1
    if valor == 3:
        print(f"ups, {valor=}")
        break  # O BREAK VAI PARAR O CICLO
    print(f"{valor=}")

# ===

# LISTAS
lista = [
    1,
    2,
    3,
    4,
    5,
]  # A LISTA É UMA ESTRUTURA DE DADOS QUE PODE CONTER VÁRIOS VALORES, ELES SÃO ORDENADOS E MUTÁVEIS
print(f"{lista=}")

for item in lista:
    print(f"{item=}")

tamanho = len(lista)  # A FUNÇÃO LEN RETORNA O TAMANHO DA LISTA
print(f"{tamanho=}")

# for i in range(len(lista)):
#     print(f"{i=}, {lista[i]=}")

i = 0
while i < len(lista):
    print(f"{i=}, {lista[i]=}")
    i += 1

lista_variada = [1, "dois", 3.0, [4, 5]]  # A LISTA PODE CONTER VÁRIOS TIPOS DE DADOS
print(f"{lista_variada=}")

print(f"{lista[-1]=}")  # O ÍNDICE NEGATIVO COMEÇA A CONTAR DO FINAL DA LISTA

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

# MÉTODOS DE LISTA
print(f"{lista=}")

lista[0] = 10  # AS LISTAS SÃO MUTÁVEIS, ENTÃO É POSSÍVEL ALTERAR O VALOR DE UM ELEMENTO
print(f"{lista=}")

lista.append(6)  # O MÉTODO APPEND ADICIONA UM ELEMENTO NO FINAL DA LISTA
print(f"{lista=}")

lista.insert(0, 0)  # O MÉTODO INSERT ADICIONA UM ELEMENTO EM UMA POSIÇÃO ESPECÍFICA
print(f"{lista=}")

lista.remove(3)  # O MÉTODO REMOVE O PRIMEIRO ELEMENTO COM O VALOR ESPECIFICADO
print(f"{lista=}")

lista.pop()  # O MÉTODO POP REMOVE O ÚLTIMO ELEMENTO DA LISTA
print(f"{lista=}")

lista.pop(0)  # O MÉTODO POP COM UM ÍNDICE REMOVE O ELEMENTO DA POSIÇÃO ESPECIFICADA
print(f"{lista=}")

lista.clear()  # O MÉTODO CLEAR REMOVE TODOS OS ELEMENTOS DA LISTA
print(f"{lista=}")

lista.extend([7, 8, 8])  # O MÉTODO EXTEND ADICIONA VÁRIOS ELEMENTOS NO FINAL DA LISTA
print(f"{lista=}")

lista.sort()  # O MÉTODO SORT ORDENA A LISTA
print(f"{lista=}")

lista.reverse()  # O MÉTODO REVERSE INVERTE A ORDEM DA LISTA
print(f"{lista=}")

lista.count(
    8
)  # O MÉTODO COUNT RETORNA O NÚMERO DE VEZES QUE UM ELEMENTO APARECE NA LISTA
print(f"{lista.count(8)=}")

lista.index(
    8
)  # O MÉTODO INDEX RETORNA O ÍNDICE DO PRIMEIRO ELEMENTO COM O VALOR ESPECIFICADO
print(f"{lista.index(8)=}")

lista_2 = lista.copy()  # O MÉTODO COPY RETORNA UMA CÓPIA DA LISTA
print(f"{lista_2=}")

lista = [1, 2, 3, 4, 5]
print(f"{lista=}")

# MATRIZES
matriz = [  # A MATRIZ É UMA LISTA DE LISTAS, ONDE CADA ELEMENTO É UMA LINHA DA MATRIZ
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"],
]

print(f"{matriz=}")
print(f"{matriz[0]=}, {matriz[1]=}, {matriz[2]=}")
print(f"{matriz[0][0]=}, {matriz[0][1]=}, {matriz[0][2]=}")

# EXERCÍCIO: VALIDAR LISTA DE PRESENÇAS

presencas = [
    "presente",
    "presente",
    "falta",
    "presente",
    "falta",
    "present",
    "presente",
    "falta!",
    "falta",
    "presente,",
    "falta",
]

for pres in presencas:
    if pres != "presente" and pres != "falta":
        # if not (pres == "presente" or pres == "falta"):
        # if pres not in ["presente", "falta"]:
        print(f"Valor inválido encontrado: {pres}")

# EXERCÍCIO: REMOVER VALORES INVÁLIDOS DA LISTA DE PRESENÇAS

presencas = [
    "presente",
    "presente",
    "falta",
    "presente",
    "falta",
    "present",
    "presente",
    "falta!",
    "falta",
    "presete,",
    "falta",
]

# i = 0
# while i < len(presencas):
#     if presencas[i] != "presente" and presencas[i] != "falta":
#         presencas.pop(i)
#     else:
#         i += 1
# print(f"{presencas=}")

# for pres, i in enumerate(presencas):
#     if pres != "presente" and pres != "falta":
#         presencas.pop(i)

presencas_validas = []  # A NOVA LISTA VAI CONTER APENAS AS PRESENÇAS VÁLIDAS, NÃO VAI ALTERAR A LISTA ORIGINAL
for pres in presencas:
    if pres != "presente" and pres != "falta":
        presencas_validas.append(pres)
print(f"{presencas_validas=}")

# ===

lista_array = [1, 2, 3, 4, 5]
lista_tuple = (1, 2, 3, 4, 5)  # A TUPLA É UMA ESTRUTURA DE DADOS SEMELHANTE À LISTA, MAS É IMUTÁVEL
lista_set = {1, 2, 3, 4, 5}  # O SET É UMA ESTRUTURA DE DADOS QUE NÃO PERMITE ELEMENTOS DUPLICADOS E NÃO TEM ORDEM
lista_dicionario = {  # O DICIONÁRIO É UMA ESTRUTURA DE DADOS QUE ARMAZENA PARES DE CHAVE-VALOR
    "um": 1,
    "dois": 2,
    "três": 3,
    "quatro": 4,
    "cinco": 5,
}
print(f"{lista_array=}, {lista_tuple=}, {lista_set=}, {lista_dicionario=}")

print(f"{lista_array[0]=}")  # A LISTA PERMITE ACESSAR OS ELEMENTOS PELO ÍNDICE
print(f"{lista_tuple[0]=}")  # A TUPLA PERMITE ACESSAR OS ELEMENTOS PELO ÍNDICE

print(f"{lista_set=}")  # O SET NÃO PERMITE ACESSAR OS ELEMENTOS PELO ÍNDICE, MAS PODE ITERAR
lista_set.add(6)  # O SET PERMITE ADICIONAR ELEMENTOS, MAS NÃO PERMITE DUPLICADOS
for elemento in lista_set:
    print(f"{elemento=}")

print(f"{lista_dicionario['um']=}")  # O DICIONÁRIO PERMITE ACESSAR OS VALORES PELAS CHAVES
del lista_dicionario["um"]  # O DICIONÁRIO PERMITE REMOVER PARES DE CHAVE-VALOR
print(f"{lista_dicionario=}")

lista_dicionario["seis"] = 6  # O DICIONÁRIO PERMITE ADICIONAR PARES DE CHAVE-VALOR
print(f"{lista_dicionario=}")

# EXERCÍCIO: CONTAR A FREQUÊNCIA DE CADA ELEMENTO EM UMA LISTA
lista_nomes = ["Rui", "Sara", "Luís", "Luís", "Rui", "Luíza", "Sara"]
frequencia = {}
for nome in lista_nomes: # O OPERADOR IN É USADO PARA VER SE UMA CHAVE EXISTE NO DICIONÁRIO, DEVOLVE TRUE SE EXISTIR E FALSE SE NÃO EXISTIR
    if nome in frequencia:
        frequencia[nome] += 1
    else:
        frequencia[nome] = 1
print(f"{frequencia=}")