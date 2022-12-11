from buscadores.utils import expande, Node


def dfs(estado_inicial):
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
        v = f.pop()

        if v.estado == ESTADO_FINAL:
            solution = []
            while v:
                solution.append(v.acao)
                v = v.pai
            return solution[-2::-1]
        
        if v.estado not in x:
            x.add(v.estado)
            f.extend(expande(v))

    raise ValueError("TILT")