# Problema das 8 Rainhas ♛

Solução para o problema das 8 rainhas utilizando busca em profundidade (DFS) com backtracking.

## Índice

- [Formulação do Problema](#formulação-do-problema)
- [Técnica Utilizada: Busca em Profundidade com Backtracking](#técnica-utilizada-busca-em-profundidade-com-backtracking)
- [Estrutura do Código](#estrutura-do-código)
- [Principais Trechos do Código](#principais-trechos-do-código)
- [Resultados Obtidos](#resultados-obtidos)
- [Como Executar](#como-executar)
- [Como a IA Auxiliou no Desenvolvimento](#como-a-ia-auxiliou-no-desenvolvimento)

---

## ♟️ Formulação do Problema

O problema das 8 rainhas consiste em posicionar 8 rainhas em um tabuleiro de xadrez 8×8 de forma que nenhuma rainha ataque outra. Uma rainha ataca outra quando estão na mesma linha, mesma coluna ou mesma diagonal.

**Representação adotada:**
- Cada coluna do tabuleiro recebe exatamente uma rainha.
- O estado é representado por uma lista de objetos `Coluna`, onde cada objeto guarda o nome da coluna e a linha em que a rainha foi posicionada.
- Como cada coluna recebe no máximo uma rainha, o conflito de colunas é eliminado por construção, restando verificar apenas conflitos de linha e diagonal.

**Restrições verificadas:**
- Duas rainhas não podem estar na mesma linha.
- Duas rainhas não podem estar na mesma diagonal: `|linha_i - linha_j| == |col_i - col_j|`.

O problema aceita um tabuleiro vazio ou com até 3 rainhas pré-colocadas nas primeiras colunas, desde que essas rainhas não estejam em ataque entre si.

---

## 💡 Técnica Utilizada: Busca em Profundidade com Backtracking

O algoritmo utilizado é a **busca em profundidade (DFS)** com **backtracking**.

A busca percorre o espaço de estados coluna a coluna, tentando posicionar uma rainha em cada linha (1 a 8). Quando encontra um conflito, descarta aquele caminho e tenta a próxima linha. Se nenhuma linha for válida para a coluna atual, retorna `False` para a coluna anterior e tenta outra posição lá — isso é o backtracking.

**Por que não força bruta?**  
A força bruta geraria 8⁸ = 16.777.216 combinações. O backtracking poda ramos inválidos assim que detecta um conflito, tornando a busca muito mais eficiente.

**Árvore de busca (simplificada):**
```
Coluna 1: tenta linha 1
  Coluna 2: linha 1 → choque, linha 2 → choque, linha 3 ✓
    Coluna 3: todas as linhas falham
  ← backtrack para Coluna 2: tenta linha 4 ✓
    Coluna 3: linha 2 ✓
      Coluna 4: ...
```

---

## 📁 Estrutura do Código

```
├── main.py           # Ponto de entrada, interface com o usuário
└── src/
    ├── no.py         # Classe Coluna (representa uma rainha posicionada)
    ├── choque.py     # Funções de verificação de conflito
    └── resolve.py    # Algoritmo de backtracking (DFS)
```

---

## 💻 Principais Trechos do Código

### Classe Coluna (`src/no.py`)
Representa uma rainha posicionada em uma coluna e linha específicas.

```python
class Coluna():
    def __init__(self, nome, linha):
        self.nome = nome
        self.linha = linha
```

### Verificação de Conflito (`src/choque.py`)
Verifica se há conflito de linha ou diagonal entre qualquer par de rainhas na lista.

```python
def verifica_choque(lista):
    for i, num in enumerate(lista):
        for j, num1 in enumerate(lista):
            if i == j:
                continue
            if choque_linha(num, num1) or choque_diagonal(num, i, num1, j):
                return True
    return False
```

O índice `i` corresponde à coluna, portanto `abs(col_i - col_j)` é simplesmente `abs(i - j)`.

### Algoritmo de Backtracking (`src/resolve.py`)
Tenta posicionar uma rainha em cada linha da coluna atual. Se nenhuma linha for válida, retorna `False` para que a coluna anterior tente outra posição.

```python
def resolver(coluna, lista):
    if coluna > 8:
        return True
    for linha in range(1, 9):
        lista.append(Coluna(f"C{coluna}", linha))
        if not verifica_choque(lista):
            if resolver(coluna + 1, lista):
                return True
        lista.pop()
    return False
```

### Interface com o Usuário (`main.py`)
Permite pré-colocar rainhas nas primeiras colunas antes de iniciar o backtracking.

```python
qtd = int(input("Quantas rainhas deseja pré-colocar? (0 a 3): "))

lista = []
for i in range(qtd):
    linha = int(input(f"Linha da rainha na coluna {i + 1} (1 a 8): "))
    lista.append(Coluna(f"C{i + 1}", linha))

if verifica_choque(lista):
    print("As rainhas pré-colocadas estão em ataque. Tente outras posições.")
else:
    if resolver(qtd + 1, lista):
        ...
```

---

## ✅ Resultados Obtidos

### Tabuleiro vazio
```
Entrada: 0 rainhas pré-colocadas
Solução: [1, 5, 8, 6, 3, 7, 2, 4]

 Q  .  .  .  .  .  .  . 
 .  .  .  .  .  .  Q  . 
 .  .  .  .  Q  .  .  . 
 .  .  .  .  .  .  .  Q 
 .  Q  .  .  .  .  .  . 
 .  .  .  Q  .  .  .  . 
 .  .  .  .  .  Q  .  . 
 .  .  Q  .  .  .  .  . 
```

### Tabuleiro com 1 rainha (coluna 1, linha 4)
```
Entrada: C1 → linha 4
Solução: [4, 1, 5, 8, 2, 7, 3, 6]

 .  Q  .  .  .  .  .  . 
 .  .  .  .  Q  .  .  . 
 .  .  .  .  .  .  Q  . 
 Q  .  .  .  .  .  .  . 
 .  .  Q  .  .  .  .  . 
 .  .  .  .  .  .  .  Q 
 .  .  .  .  .  Q  .  . 
 .  .  .  Q  .  .  .  . 
```

### Tabuleiro com 2 rainhas (coluna 1 linha 2, coluna 2 linha 5)
```
Entrada: C1 → linha 2, C2 → linha 5
Solução: [2, 5, 7, 1, 3, 8, 6, 4]

 .  .  .  Q  .  .  .  . 
 Q  .  .  .  .  .  .  . 
 .  .  .  .  Q  .  .  . 
 .  .  .  .  .  .  .  Q 
 .  Q  .  .  .  .  .  . 
 .  .  .  .  .  .  Q  . 
 .  .  Q  .  .  .  .  . 
 .  .  .  .  .  Q  .  . 
```

### Tabuleiro com 3 rainhas (coluna 1 linha 1, coluna 2 linha 6, coluna 3 linha 8)
```
Entrada: C1 → linha 1, C2 → linha 6, C3 → linha 8
Solução: [1, 6, 8, 3, 7, 4, 2, 5]

 Q  .  .  .  .  .  .  . 
 .  .  .  .  .  .  Q  . 
 .  .  .  Q  .  .  .  . 
 .  .  .  .  .  Q  .  . 
 .  .  .  .  .  .  .  Q 
 .  Q  .  .  .  .  .  . 
 .  .  .  .  Q  .  .  . 
 .  .  Q  .  .  .  .  . 
```

> **Obs.:** caso as rainhas pré-colocadas tornem impossível completar o tabuleiro, o programa informa "Sem solução para as rainhas pré-colocadas escolhidas."

---

## ▶️ Como Executar

```bash
python3 main.py
```

Siga as instruções no terminal: informe quantas rainhas deseja pré-colocar (0 a 3) e, para cada uma, a linha desejada (1 a 8).

---

## 🤖 Como a IA Auxiliou no Desenvolvimento

O desenvolvimento contou com o auxílio do **Claude (Anthropic)** como ferramenta de revisão e aprendizado. A IA não escreveu o código — o aluno implementou a solução — mas contribuiu das seguintes formas:

- **Diagnóstico do código original:** identificou que o `rainha.py` inicial não tinha backtracking, o que impedia encontrar soluções completas de forma confiável.
- **Explicação do algoritmo:** explicou o conceito de busca em profundidade (DFS) com backtracking e como ele se aplica ao problema das 8 rainhas.
- **Revisão de código:** após cada implementação do aluno, apontou os bugs encontrados (falta de `def`, função não chamada, `list.pop()` com argumento incorreto, `range` errado, import incorreto) sem reescrever o código.
- **Correção de imports:** após a reorganização dos arquivos para a pasta `src/`, identificou o problema com `from no import Coluna` e aplicou a correção para imports relativos (`from .no import Coluna`).
- **Implementação da interface:** a pedido do aluno, implementou a parte do `main.py` responsável por perguntar quantas rainhas pré-colocar e em qual linha cada uma deve ficar.
