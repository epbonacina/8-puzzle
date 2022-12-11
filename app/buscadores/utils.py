ESTADO_FINAL = "12345678_"


class Node:
    def __init__(self, estado, pai, acao, custo):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo

    def __repr__(self):
        return f"Node(estado={self.estado}, pai={self.pai}, acao={self.acao}, custo={self.custo})"


def _swap(estado, idx_1, idx_2):
    novo_estado = list(estado)

    novo_estado[idx_1], novo_estado[idx_2] = novo_estado[idx_2], novo_estado[idx_1]
    novo_estado = "".join(novo_estado)

    return novo_estado


def sucessor(estado):
    espaco_idx = estado.index("_")

    sucessores = {}

    if espaco_idx in {3,4,5,6,7,8}:
        sucessores["cima"] = _swap(estado, espaco_idx, espaco_idx-3)

    if espaco_idx in {0,1,2,3,4,5}:
        sucessores["baixo"] = _swap(estado, espaco_idx, espaco_idx+3)

    if espaco_idx in {0,1,3,4,6,7}:
        sucessores["direita"] = _swap(estado, espaco_idx, espaco_idx+1)

    if espaco_idx in {1,2,4,5,7,8}:
        sucessores["esquerda"] = _swap(estado, espaco_idx, espaco_idx-1)

    return list(sucessores.items())
    

def expande(nodo):
    sucessores = sucessor(nodo.estado)
    filhos = [Node(estado, nodo, acao, nodo.custo + 1) for acao, estado in sucessores]

    return filhos


def busca_grafo(func_remocao, func_insercao, estado_inicial):
    x = set()
    f = [
        Node(
            estado = estado_inicial, 
            pai = None, 
            acao = None, 
            custo = 0
        )
    ]

    while True:
        if not f:
            return len(x), None
            
        v = func_remocao(f)
        if v.estado == ESTADO_FINAL:
            solution = []
            while v:
                solution.append(v.acao)
                v = v.pai
            return len(x), solution[-2::-1]
        
        if v.estado not in x:
            x.add(v.estado)
            f = func_insercao(f, expande(v))
