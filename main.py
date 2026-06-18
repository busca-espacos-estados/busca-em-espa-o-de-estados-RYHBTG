"""Script de demonstração — útil para depurar manualmente."""

from puzzle.state import State
from algorithms.bfs import BFS
from algorithms.dfs import DFS
from algorithms.a_star import AStar


def print_result(name: str, result):
    print(f"\n{'='*40}")
    print(f"Algoritmo : {name}")
    if result.found:
        print(f"Solução   : {' -> '.join(result.actions)}")
        print(f"Custo     : {result.path_cost}")
        print(f"Profund.  : {result.depth}")
    else:
        print("Solução   : NÃO ENCONTRADA")
    print(f"Expandidos: {result.nodes_expanded}")
    print(f"Gerados   : {result.nodes_generated}")
    print(f"Fronteira : {result.max_frontier_size} (máx)")


if __name__ == "__main__":
    initialnaofuncional = State((2, 8, 3, 1, 6, 4, 7, 0, 5))   

    print("Estado inicial:")
    print(initialnaofuncional)

    print_result("BFS",  BFS().search(initialnaofuncional))
    print_result("DFS",  DFS().search(initialnaofuncional))
    print_result("A*",   AStar().search(initialnaofuncional))

    print("\n" + "="*40 + "\n")

    initialfuncional = State((2, 8, 1, 3, 6, 4, 7, 0, 5)) # Trocando o 1 e o 3 de lugar para que funcione
    print("Estado inicial:")
    print(initialfuncional)

    print_result("BFS",  BFS().search(initialfuncional))
    print_result("DFS",  DFS().search(initialfuncional))
    print_result("A*",   AStar().search(initialfuncional))
