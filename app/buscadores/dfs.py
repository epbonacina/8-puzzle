from buscadores.utils import busca_grafo


def dfs(estado_inicial):
    return busca_grafo(remove_da_fila, insere_na_fila, estado_inicial)


def remove_da_fila(fila):
    return fila.pop()


def insere_na_fila(fila, novos_nodos):
    fila.extend(novos_nodos)
    return fila
