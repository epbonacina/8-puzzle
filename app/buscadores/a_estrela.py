import bisect

from buscadores.utils import busca_grafo, ESTADO_FINAL


def a_estrela_manhattan(estado_inicial):
    return busca_grafo(remove_da_fila, insere_na_fila_usando_distancia_manhattan, estado_inicial)


def remove_da_fila(fila):
    return fila.pop(0)


def insere_na_fila_usando_distancia_manhattan(fila, novos_nodos):
    for nodo in novos_nodos:
        bisect.insort(fila, nodo, key=get_custo_mais_distancia_manhattan)
    return fila


def get_custo_mais_distancia_manhattan(nodo):
    return nodo.custo + distancia_manhattan(nodo.estado)


def distancia_manhattan(estado):
    tabuleiro = [int(v) for v in estado.replace("_", "0")]
    
    distancia = sum(abs((valor-1)%3 - i%3) + abs((valor-1)//3 - i//3)
        for i, valor in enumerate(tabuleiro) if valor)

    return distancia


def a_estrela_hamming(estado_inicial):
    return busca_grafo(remove_da_fila, insere_na_fila_usando_distancia_hamming, estado_inicial)


def insere_na_fila_usando_distancia_hamming(fila, novos_nodos):
    for nodo in novos_nodos:
        bisect.insort(fila, nodo, key=get_custo_mais_distancia_hamming)
    return fila


def get_custo_mais_distancia_hamming(nodo):
    return nodo.custo + distancia_hamming(nodo.estado)


def distancia_hamming(estado):
    distancia = sum([1 for valor in estado if estado.index(valor) != ESTADO_FINAL.index(valor)])

    return distancia