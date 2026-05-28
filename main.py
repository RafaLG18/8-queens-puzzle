from src.resolve import resolver
from src.no import Coluna
from src.choque import verifica_choque

qtd = int(input("Quantas rainhas deseja pré-colocar? (0 a 3): "))

lista = []
for i in range(qtd):
    linha = int(input(f"Linha da rainha na coluna {i + 1} (1 a 8): "))
    lista.append(Coluna(f"C{i + 1}", linha))

if verifica_choque(lista):
    print("As rainhas pré-colocadas estão em ataque. Tente outras posições.")
else:
    if resolver(qtd + 1, lista):
        solucao = [coluna.linha for coluna in lista]
        print(solucao)
        for linha in range(1, 9):
            row = ""
            for col in range(8):
                row += " Q " if solucao[col] == linha else " . "
            print(row)
    else:
        print("Sem solução para as rainhas pré-colocadas escolhidas.")
