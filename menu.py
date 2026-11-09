"""PARTE 6 - Interface de menu (console).

Mostra as opcoes, le a escolha do usuario e chama os outros modulos.
Nenhuma entrada do usuario pode derrubar o programa.
"""
import graficos
import indicadores
import relatorio


def mostrar_menu():
    """Imprime as opcoes do menu."""
    print("\n=========== PAINEL DE VENDAS ===========")
    print("1 - Ver indicadores na tela")
    print("2 - Gerar graficos (PNG)")
    print("3 - Gerar relatorio (Markdown)")
    print("4 - Faturamento por... (categoria/regiao/vendedor)")
    print("0 - Sair")


def ler_opcao():
    """Le a opcao digitada; devolve um inteiro ou -1 se for invalida."""
    texto = input("Escolha uma opcao: ").strip()
    try:
        return int(texto)
    except ValueError:
        return -1


def mostrar_indicadores(df):
    """Opcao 1: imprime os principais numeros."""
    print(f"\nFaturamento total: {relatorio.moeda(indicadores.faturamento_total(df))}")
    print(f"Ticket medio:      {relatorio.moeda(indicadores.ticket_medio(df))}")
    nome, valor = indicadores.melhor_vendedor(df)
    print(f"Melhor vendedor:   {nome} ({relatorio.moeda(valor)})")
    print("\nTop 5 produtos:")
    for produto, valor in indicadores.top_produtos(df, 5).items():
        print(f"  - {produto:<18} {relatorio.moeda(valor):>16}")


def mostrar_agrupado(df):
    """Opcao 4: pergunta o criterio e imprime o faturamento agrupado."""
    opcoes = {"1": "categoria", "2": "regiao", "3": "vendedor"}
    print("1 - Categoria   2 - Regiao   3 - Vendedor")
    escolha = input("Agrupar por: ").strip()
    if escolha not in opcoes:
        print(">> Opcao invalida.")
        return
    for nome, valor in indicadores.faturamento_por(df, opcoes[escolha]).items():
        print(f"  - {nome:<14} {relatorio.moeda(valor):>16}")


def executar(df, resumo):
    """Laco principal do menu: roda ate o usuario escolher 0."""
    while True:
        mostrar_menu()
        opcao = ler_opcao()
        if opcao == 0:
            print("Ate logo!")
            break
        elif opcao == 1:
            mostrar_indicadores(df)
        elif opcao == 2:
            for funcao in (graficos.grafico_por_categoria,
                           graficos.grafico_evolucao_mensal,
                           graficos.grafico_top_produtos):
                print(f">> Grafico salvo em {funcao(df)}")
        elif opcao == 3:
            print(f">> Relatorio salvo em {relatorio.gerar_relatorio(df, resumo)}")
        elif opcao == 4:
            mostrar_agrupado(df)
        else:
            print(">> Opcao invalida. Tente de novo.")
