"""PARTE 2 - Carga e limpeza dos dados (pandas).

Le o CSV e entrega um DataFrame confiavel: sem duplicados, sem linhas
invalidas, com tipos corretos e uma coluna nova de faturamento.
"""
import pandas as pd

import configuracao


def carregar_vendas():
    """Le o CSV de vendas e devolve (dataframe_limpo, resumo_da_limpeza)."""
    try:
        bruto = pd.read_csv(configuracao.CAMINHO_CSV)
    except FileNotFoundError:
        raise SystemExit(f"Arquivo nao encontrado: {configuracao.CAMINHO_CSV}")

    faltando = [c for c in configuracao.COLUNAS_OBRIGATORIAS
                if c not in bruto.columns]
    if faltando:
        raise SystemExit(f"Colunas ausentes no CSV: {faltando}")

    limpo = limpar(bruto)
    resumo = {
        "linhas_lidas": len(bruto),
        "linhas_validas": len(limpo),
        "linhas_descartadas": len(bruto) - len(limpo),
    }
    return limpo, resumo


def limpar(df):
    """Remove duplicados e linhas invalidas, ajusta tipos e cria faturamento."""
    df = df.drop_duplicates()

    # errors="coerce" transforma valores ruins em NaN em vez de dar erro
    df = df.assign(
        data=pd.to_datetime(df["data"], errors="coerce"),
        quantidade=pd.to_numeric(df["quantidade"], errors="coerce"),
        preco_unitario=pd.to_numeric(df["preco_unitario"], errors="coerce"),
    )
    df = df.dropna(subset=["data", "quantidade", "preco_unitario"])

    df = df.assign(quantidade=df["quantidade"].astype(int))
    df = df.assign(faturamento=df["quantidade"] * df["preco_unitario"])
    df = df.assign(mes=df["data"].dt.to_period("M").astype(str))
    return df.reset_index(drop=True)
