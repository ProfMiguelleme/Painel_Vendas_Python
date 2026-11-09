"""Gera dados/vendas.csv com vendas ficticias da loja TechSul.

Roda uma vez (ja vem rodado). Usa so a biblioteca padrao.
Inclui de proposito algumas linhas "sujas" para a limpeza (parte 2) tratar.
"""
import csv
import random
from datetime import date, timedelta

random.seed(42)

PRODUTOS = [
    ("Notebook 15", "Computadores", 3499.90),
    ("Monitor 24", "Perifericos", 899.00),
    ("Teclado Mecanico", "Perifericos", 349.90),
    ("Mouse Sem Fio", "Perifericos", 89.90),
    ("Webcam Full HD", "Perifericos", 199.90),
    ("Cadeira Gamer", "Moveis", 1290.00),
    ("Mesa Escritorio", "Moveis", 780.00),
    ("Headset USB", "Audio", 159.90),
]
REGIOES = ["Sul", "Sudeste", "Nordeste", "Centro-Oeste"]
VENDEDORES = ["Ana", "Bruno", "Carla", "Diego"]

linhas = []
inicio = date(2026, 1, 1)
for i in range(1, 241):
    nome, cat, preco = random.choice(PRODUTOS)
    dia = inicio + timedelta(days=random.randint(0, 299))
    linhas.append([i, dia.strftime("%Y-%m-%d"), nome, cat,
                   random.randint(1, 5), preco,
                   random.choice(REGIOES), random.choice(VENDEDORES)])

# linhas sujas de proposito
linhas[10][4] = ""            # quantidade vazia
linhas[25][5] = ""            # preco vazio
linhas[40][1] = "data-invalida"
linhas.append(list(linhas[5]))  # linha duplicada

with open("dados/vendas.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["id", "data", "produto", "categoria", "quantidade",
                "preco_unitario", "regiao", "vendedor"])
    w.writerows(linhas)
print(f"{len(linhas)} linhas gravadas em dados/vendas.csv")
