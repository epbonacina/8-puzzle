from buscadores.utils import Queue, busca_grafo


def bfs(nodo):
    return busca_grafo(nodo, Queue())
