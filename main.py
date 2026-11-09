"""Painel de Vendas TechSul - ponto de entrada do programa.

Fluxo: prepara pastas -> carrega e limpa os dados -> abre o menu.
Para rodar:  python main.py
"""
import configuracao
import dados
import menu


def main():
    configuracao.preparar_pastas()
    df, resumo = dados.carregar_vendas()
    print(f">> {resumo['linhas_validas']} vendas carregadas "
          f"({resumo['linhas_descartadas']} linha(s) descartada(s) na limpeza).")
    menu.executar(df, resumo)


if __name__ == "__main__":
    main()
