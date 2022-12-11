from buscadores.utils import expande, Node


def bfs(estado_inicial):
    ESTADO_FINAL = "12345678_"

    x = set()
    f = [
        Node(
            estado = estado_inicial, 
            pai = None, 
            acao = "null", 
            custo = 0
        )
    ]

    while f:
        v = f.pop(0)

        if v.estado == ESTADO_FINAL:
            solution = []
            while v:
                solution.append(v.acao)
                v = v.pai
            return len(x), solution[-2::-1]
        
        if v.estado not in x:
            x.add(v.estado)
            f.extend(expande(v))

    return len(x), None