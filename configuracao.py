"""PARTE 1 - Configuracao e orquestracao (main.py usa este modulo).

Define onde ficam os arquivos e prepara as pastas de saida.
Centralizar caminhos num so lugar evita "strings magicas" espalhadas.
"""
from pathlib import Path

PASTA_BASE = Path(__file__).parent
CAMINHO_CSV = PASTA_BASE / "dados" / "vendas.csv"
PASTA_SAIDA = PASTA_BASE / "saida"

COLUNAS_OBRIGATORIAS = [
    "id", "data", "produto", "categoria",
    "quantidade", "preco_unitario", "regiao", "vendedor",
]


def preparar_pastas():
    """Cria a pasta de saida se ela ainda nao existir."""
    PASTA_SAIDA.mkdir(exist_ok=True)


def caminho_saida(nome_arquivo):
    """Devolve o caminho completo de um arquivo dentro da pasta de saida."""
    return PASTA_SAIDA / nome_arquivo
