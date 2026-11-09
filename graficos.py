"""PARTE 4 - Graficos (matplotlib).

Cada funcao cria um grafico, salva um PNG na pasta saida/ e devolve
o caminho do arquivo.
"""
import matplotlib
matplotlib.use("Agg")  # gera imagens sem abrir janela (funciona em qualquer PC)
import matplotlib.pyplot as plt

import configuracao
import indicadores


def grafico_por_categoria(df):
    """Barras: faturamento por categoria."""
    dados = indicadores.faturamento_por(df, "categoria")
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(dados.index, dados.values, color="#2E6DA4")
    ax.set_title("Faturamento por categoria")
    ax.set_ylabel("R$")
    return _salvar(fig, "grafico_categoria.png")


def grafico_evolucao_mensal(df):
    """Linha: faturamento mes a mes."""
    dados = indicadores.faturamento_por(df, "mes")
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(dados.index, dados.values, marker="o", color="#1F3A5F")
    ax.set_title("Evolucao do faturamento mensal")
    ax.set_ylabel("R$")
    ax.tick_params(axis="x", rotation=45)
    return _salvar(fig, "grafico_mensal.png")


def grafico_top_produtos(df):
    """Barras horizontais: top 5 produtos."""
    dados = indicadores.top_produtos(df, 5).sort_values()
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.barh(dados.index, dados.values, color="#2E6DA4")
    ax.set_title("Top 5 produtos por faturamento")
    ax.set_xlabel("R$")
    return _salvar(fig, "grafico_top_produtos.png")


def _salvar(fig, nome_arquivo):
    """Funcao interna: ajusta, grava o PNG e libera a memoria da figura."""
    caminho = configuracao.caminho_saida(nome_arquivo)
    fig.tight_layout()
    fig.savefig(caminho, dpi=120)
    plt.close(fig)
    return caminho
