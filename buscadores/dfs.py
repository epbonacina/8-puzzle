from buscadores.utils import Stack, busca_grafo


def dfs(nodo):
    return busca_grafo(nodo, Stack())
