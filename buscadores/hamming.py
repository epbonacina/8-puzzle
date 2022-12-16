from buscadores.utils import AStar, busca_grafo


def hamming_heuristic(item):
    goal = "12345678_"
    state = item.estado
    sum = 0
    for i, v in enumerate(goal):
        if v != state[i]:
            sum += 1
    return sum


def hamming(nodo):
    return busca_grafo(nodo, AStar(hamming_heuristic))
