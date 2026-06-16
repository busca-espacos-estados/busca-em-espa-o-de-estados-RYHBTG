import heapq
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult


class AStar(BaseSearch):

    def heuristic(self, state: State) -> int:
        distance = 0
        for index, tile in enumerate(state.tiles):
            if tile == 0:
                continue
            target_row, target_col = divmod(tile - 1, 3)
            current_row, current_col = divmod(index, 3)
            distance += abs(target_row - current_row) + abs(target_col - current_col)
        return distance

    def search(self, initial: State) -> SearchResult:
        open_heap = []
        heapq.heappush(open_heap, (self.heuristic(initial), 0, initial))
        g_scores = {initial: 0}
        nodes_expanded = 0
        nodes_generated = 1
        max_frontier_size = 1

        while open_heap:
            max_frontier_size = max(max_frontier_size, len(open_heap))
            _, g, state = heapq.heappop(open_heap)

            if g > g_scores.get(state, float("inf")):
                continue

            nodes_expanded += 1

            if state.is_goal:
                return SearchResult(
                    solution=state,
                    nodes_expanded=nodes_expanded,
                    nodes_generated=nodes_generated,
                    max_frontier_size=max_frontier_size,
                    depth=len(state.actions()),
                )

            for neighbor in state.neighbors():
                tentative_g = g + 1
                if tentative_g < g_scores.get(neighbor, float("inf")):
                    g_scores[neighbor] = tentative_g
                    neighbor.cost = tentative_g
                    heapq.heappush(open_heap, (tentative_g + self.heuristic(neighbor), tentative_g, neighbor))
                    nodes_generated += 1

        return SearchResult(
            solution=None,
            nodes_expanded=nodes_expanded,
            nodes_generated=nodes_generated,
            max_frontier_size=max_frontier_size,
            depth=0,
        )
