"""PARTE 5 - Relatorio em arquivo (texto + f-strings).

Monta um relatorio Markdown com os indicadores e grava em saida/.
"""
from datetime import datetime

import configuracao
import indicadores


def moeda(valor):
    """Formata em reais: 1234.5 -> 'R$ 1.234,50'."""
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


def montar_texto(df, resumo):
    """Monta o relatorio inteiro em uma unica string."""
    nome_vend, valor_vend = indicadores.melhor_vendedor(df)
    linhas = [
        "# Relatorio de Vendas - TechSul",
        f"Gerado em {datetime.now():%d/%m/%Y %H:%M}",
        "",
        "## Qualidade dos dados",
        f"- Linhas lidas: {resumo['linhas_lidas']}",
        f"- Linhas validas: {resumo['linhas_validas']}",
        f"- Linhas descartadas: {resumo['linhas_descartadas']}",
        "",
        "## Indicadores",
        f"- Faturamento total: {moeda(indicadores.faturamento_total(df))}",
        f"- Ticket medio: {moeda(indicadores.ticket_medio(df))}",
        f"- Melhor vendedor: {nome_vend} ({moeda(valor_vend)})",
        "",
        "## Top 5 produtos",
    ]
    for posicao, (produto, valor) in enumerate(
            indicadores.top_produtos(df, 5).items(), start=1):
        linhas.append(f"{posicao}. {produto}: {moeda(valor)}")
    linhas.append("")
    linhas.append("## Faturamento por regiao")
    for regiao, valor in indicadores.faturamento_por(df, "regiao").items():
        linhas.append(f"- {regiao}: {moeda(valor)}")
    return "\n".join(linhas) + "\n"


def gerar_relatorio(df, resumo):
    """Grava o relatorio em saida/relatorio_vendas.md e devolve o caminho."""
    caminho = configuracao.caminho_saida("relatorio_vendas.md")
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(montar_texto(df, resumo))
    return caminho
