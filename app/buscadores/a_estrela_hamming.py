from queue import PriorityQueue

from buscadores.utils import expande, Node

ESTADO_FINAL = "12345678_"


def a_estrela_hamming(estado_inicial):

    x = set()
    fronteira = PriorityQueue()
    fronteira.put(
        (
            distancia_hamming(estado_inicial),
            Node(
                estado = estado_inicial, 
                pai = None, 
                acao = "null", 
                custo = 0
            )
        )
    )

    while not fronteira.empty():
        v = fronteira.get()[1]

        if v.estado == ESTADO_FINAL:
            solution = []
            while v:
                solution.append(v.acao)
                v = v.pai
            return len(x), solution[-2::-1]
        
        if v.estado not in x:
            x.add(v.estado)
            for filho in expande(v):
                fronteira.put((filho.custo + distancia_hamming(filho.estado), filho))

    return len(x), None


def distancia_hamming(estado):
    distancia = sum([1 for valor in estado if estado.index(valor) != ESTADO_FINAL.index(valor)])

    return distancia
    