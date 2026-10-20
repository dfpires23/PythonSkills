# 1 - Calcula a média destes valores:
#     1, 4, 5, 63, 44, 20, 4, 2, 1, 10, 10

valores = [1, 4, 5, 63, 44, 20, 4, 2, 1, 10, 10]
soma = 0
for v in valores:
    soma += v
media = soma / len(valores)
print(f"Média = {media:.2f}")

# 2 - Filtra esta lista para apenas devolver valores maiores que 10.
#         1, 4, 5, 63, 44, 20, 4, 2, 1, 10, 10

valores = [1, 4, 5, 63, 44, 20, 4, 2, 1, 10, 10]
valores_maiores_que_dez = []
for v in valores:
    if v > 10:
        valores_maiores_que_dez.append(v)
print(valores_maiores_que_dez)

# 3 - Cria um dicionário com o número de faltas de cada pessoa:
#         Rui: Falta, Falta, Presença, Presença
#         Sara: Presença, Falta, Falta, Falta
#         Maria: Falta, Presença, Presença, Falta
#         Luís: Presença, Falta, Presença, Presença

arr_nomes = ["Rui", "Sara", "Maria", "Luís"]
arr_presencas = [
    ["Falta", "Falta", "Presença", "Presença"],
    ["Presença", "Falta", "Falta", "Falta"],
    ["Falta", "Presença", "Presença", "Falta"],
    ["Presença", "Falta", "Presença", "Presença"]
]
frequencia_faltas = {}
for (i, n) in enumerate(arr_nomes):
    contagem_faltas = 0
    for presenca in arr_presencas[i]:
        if presenca == "Falta":
            contagem_faltas += 1
    frequencia_faltas[n] = contagem_faltas
print(f"{frequencia_faltas=}")

# # SOLUÇÃO MAIS SIMPLES USANDO ZIP
# frequencia_faltas = {}
# for n, presencas in zip(arr_nomes, arr_presencas):
#     frequencia_faltas[n] = presencas.count("Falta")
# print(f"{frequencia_faltas=}")