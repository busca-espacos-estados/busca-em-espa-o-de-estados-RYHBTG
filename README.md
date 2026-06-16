# 8-Puzzle — Busca em Espaço de Estados

## O que implementar

### `puzzle/state.py`
- `neighbors()` — gera os estados filhos a partir do espaço vazio
- `path()` — reconstrói a sequência de estados do inicial até este
- `actions()` — retorna a sequência de ações usando `path()`

### `algorithms/bfs.py`
- `BFS.search(initial)` — Busca em Largura

### `algorithms/dfs.py`
- `DFS.search(initial)` — Busca em Profundidade

### `algorithms/a_star.py`
- `AStar.heuristic(state)` — função heurística admissível
- `AStar.search(initial)` — Busca A*

## Estrutura

```
├── puzzle/
│   ├── state.py        # State — IMPLEMENTAR neighbors, path, actions
│   ├── result.py       # SearchResult — não alterar
│   └── base_search.py  # Interface BaseSearch — não alterar
├── algorithms/
│   ├── bfs.py          ← IMPLEMENTAR
│   ├── dfs.py          ← IMPLEMENTAR
│   └── a_star.py       ← IMPLEMENTAR
└── main.py
```

## Caso impossível

O estado inicial usado no `main.py`:

```python
State((2, 8, 3, 1, 6, 4, 7, 0, 5))
```

é um caso insolúvel para o 8-puzzle clássico com objetivo:

```python
(1, 2, 3,
 4, 5, 6,
 7, 8, 0)
```

### Por que ele é insolúvel

Para o 8-puzzle, a solvabilidade é determinada pela paridade das inversões do estado.

- Conte as inversões entre os números `1..8`, ignorando o branco `0`.
- Uma inversão é um par de valores `a, b` onde `a` aparece antes de `b` e `a > b`.
- O estado é solucionável apenas se o número total de inversões for par.

No estado acima, existem `11` inversões. Como `11` é ímpar, o estado não pode ser transformado legalmente no objetivo.

### O que isso significa para os algoritmos

- `BFS`, `DFS` e `A*` não encontrarão solução porque não existe solução.
- Isso não indica que os algoritmos estão incorretos.
- Indica apenas que o problema, com esse estado inicial e esse objetivo, não é solvável.

## Referências rápidas

- 8-puzzle clássico: o número de inversões define a solvabilidade.
- Busca em largura (`BFS`) encontra o caminho mínimo em grafos não ponderados.
- Busca em profundidade (`DFS`) explora profundidade e pode achar caminho não ótimo.
- A* com heurística admissível (por exemplo, distância de Manhattan) encontra solução ótima quando ela existe.


