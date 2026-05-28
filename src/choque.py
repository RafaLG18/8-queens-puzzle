from .no import Coluna

def choque_linha(num1, num2):
    if num1.linha==num2.linha:
        return True
    else:
        return False
    return None
def choque_diagonal(num1, col1, num2, col2):
    if abs(num1.linha - num2.linha) == abs(col1 - col2):
        return True
    else:
        return False

def verifica_choque(lista):
    for i, num in enumerate(lista):
        for j, num1 in enumerate(lista):
            if i == j:
                continue
            if choque_linha(num, num1) or choque_diagonal(num, i, num1, j):
                return True
    return False
