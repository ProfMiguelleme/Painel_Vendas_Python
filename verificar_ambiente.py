"""PASSO 1 do projeto: confere se o seu computador esta pronto.

Rode:  python verificar_ambiente.py
Se tudo der OK, tire um print da tela: ele e a sua evidencia do passo 1.
"""
import sys


def checar(nome_modulo):
    try:
        modulo = __import__(nome_modulo)
        print(f"[OK]   {nome_modulo} {modulo.__version__}")
        return True
    except ImportError:
        print(f"[ERRO] {nome_modulo} nao esta instalado "
              f"(rode: pip install -r requirements.txt)")
        return False


print(f"Python {sys.version.split()[0]}")
if sys.version_info < (3, 9):
    print("[ERRO] Use Python 3.9 ou superior.")
resultados = [checar("pandas"), checar("matplotlib")]
print()
print("Ambiente pronto! Pode rodar: python main.py" if all(resultados)
      else "Ambiente incompleto: corrija os itens com [ERRO].")
