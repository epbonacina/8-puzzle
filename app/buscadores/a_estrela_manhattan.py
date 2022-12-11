from queue import PriorityQueue

from buscadores.utils import expande, Node


def a_estrela_manhattan(estado_inicial):
    ESTADO_FINAL = "12345678_"

    x = set()
    fronteira = PriorityQueue()
    fronteira.put(
        (
            distancia_manhattan(estado_inicial),
            Node(
                estado = estado_inicial, 
                pai = None, 
                acao = "null", 
                custo = 0
            )
        )
    )

    while fronteira:
        v = fronteira.get()[1]

        if v.estado == ESTADO_FINAL:
            solution = []
            while v:
                solution.append(v.acao)
                v = v.pai
            return solution[-2::-1]
        
        if v.estado not in x:
            x.add(v.estado)
            for filho in expande(v):
                fronteira.put((filho.custo + distancia_manhattan(filho.estado), filho))

    raise ValueError("TILT")


def distancia_manhattan(estado):
    tabuleiro = [int(v) for v in estado.replace("_", "0")]
    
    distancia = sum(abs((valor-1)%3 - i%3) + abs((valor-1)//3 - i//3)
        for i, valor in enumerate(tabuleiro) if valor)
    
    return distancia
    