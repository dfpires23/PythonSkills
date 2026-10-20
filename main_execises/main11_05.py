import random
import aux11_05

# ===
# DEFINIR FUNÇÕES
def escolher_nome(lista):
    nome_random = random.choice(lista)
    return nome_random


lista = ["Xavier", "Carlos", "Manuel", "Margarida", "Sofia", "Joaquim"]
nome = escolher_nome(lista)
print(f"O nome escolhido é: {nome}")

# ===
# USO DE FUNÇÕES DE OUTROS MÓDULOS
aux11_05.imprimir_intervalo()
