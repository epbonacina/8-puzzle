from buscadores.utils import AStar, busca_grafo
from buscadores import MANHATTAN_DICT


def manhattan_heuristic(item):
    state = item.estado
    total = 0
    for i, v in enumerate(state):
        total += MANHATTAN_DICT[str(i)][v]
    return total


def manhattan(nodo):
    return busca_grafo(nodo, AStar(manhattan_heuristic))
