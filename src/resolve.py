from src.choque import verifica_choque
from .no import Coluna

def resolver(coluna,lista):
    if coluna >8:
        return True
    for linha in range(1,9):
        lista.append(Coluna(f"C{coluna}",linha))
        if not verifica_choque(lista):
            if resolver(coluna+1, lista):
                return True
        lista.pop()
    return False
