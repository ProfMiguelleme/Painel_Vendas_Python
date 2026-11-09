"""PARTE 3 - Indicadores (calculos com pandas).

Toda funcao aqui so CALCULA e devolve o resultado. Quem mostra na tela
ou grava em arquivo sao outros modulos (mesma ideia "calcular vs exibir"
que voces viram na Trilha 4).
"""


def faturamento_total(df):
    """Soma de todo o faturamento."""
    return float(df["faturamento"].sum())


def ticket_medio(df):
    """Faturamento medio por venda (0.0 se nao houver vendas)."""
    if len(df) == 0:
        return 0.0
    return float(df["faturamento"].mean())


def top_produtos(df, quantidade=5):
    """Os produtos que mais faturaram, do maior para o menor."""
    return (df.groupby("produto")["faturamento"]
              .sum()
              .sort_values(ascending=False)
              .head(quantidade))


def faturamento_por(df, coluna):
    """Faturamento somado por categoria, regiao, vendedor ou mes."""
    return df.groupby(coluna)["faturamento"].sum().sort_index()


def melhor_vendedor(df):
    """Devolve (nome, faturamento) do vendedor que mais vendeu."""
    por_vendedor = faturamento_por(df, "vendedor")
    nome = por_vendedor.idxmax()
    return nome, float(por_vendedor[nome])
