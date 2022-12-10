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
    
    novo_estado_baixo = estado
    novo_estado_direita = estado
    novo_estado_esquerda = estado
    novo_estado_cima = estado

    if espaco_idx == 0:
        novo_estado_baixo = _swap(novo_estado_baixo, espaco_idx, 3)
        novo_estado_direita = _swap(novo_estado_direita, espaco_idx, 1)
        
        return [("baixo", novo_estado_baixo), ("direita", novo_estado_direita)]

    if espaco_idx == 1:
        novo_estado_baixo = _swap(novo_estado_baixo, espaco_idx, 4)
        novo_estado_direita = _swap(novo_estado_direita, espaco_idx, 2)
        novo_estado_esquerda = _swap(novo_estado_esquerda, espaco_idx, 0)
        
        return [("baixo", novo_estado_baixo), ("direita", novo_estado_direita), ("esquerda", novo_estado_esquerda)]

    if espaco_idx == 2:
        novo_estado_baixo = _swap(novo_estado_baixo, espaco_idx, 5)
        novo_estado_esquerda = _swap(novo_estado_esquerda, espaco_idx, 1)
        
        return [("baixo", novo_estado_baixo), ("esquerda", novo_estado_esquerda)]

    if espaco_idx == 3:
        novo_estado_baixo = _swap(novo_estado_baixo, espaco_idx, 6)
        novo_estado_direita = _swap(novo_estado_direita, espaco_idx, 4)
        novo_estado_cima = _swap(novo_estado_cima, espaco_idx, 0)
        
        return [("baixo", novo_estado_baixo), ("direita", novo_estado_direita), ("cima", novo_estado_cima)]

    if espaco_idx == 4:
        novo_estado_baixo = _swap(novo_estado_baixo, espaco_idx, 7)
        novo_estado_esquerda = _swap(novo_estado_esquerda, espaco_idx, 3)
        novo_estado_direita = _swap(novo_estado_direita, espaco_idx, 5)
        novo_estado_cima = _swap(novo_estado_cima, espaco_idx, 1)
        
        return [("baixo", novo_estado_baixo), ("direita", novo_estado_direita), ("cima", novo_estado_cima), ("esquerda", novo_estado_esquerda)]

    if espaco_idx == 5:
        novo_estado_baixo = _swap(novo_estado_baixo, espaco_idx, 8)
        novo_estado_esquerda = _swap(novo_estado_esquerda, espaco_idx, 4)
        novo_estado_cima = _swap(novo_estado_cima, espaco_idx, 2)
        
        return [("baixo", novo_estado_baixo), ("cima", novo_estado_cima), ("esquerda", novo_estado_esquerda)]

    if espaco_idx == 6:
        novo_estado_direita = _swap(novo_estado_direita, espaco_idx, 7)
        novo_estado_cima = _swap(novo_estado_cima, espaco_idx, 3)
        
        return [("direita", novo_estado_direita), ("cima", novo_estado_cima)]

    if espaco_idx == 7:
        novo_estado_esquerda = _swap(novo_estado_esquerda, espaco_idx, 6)
        novo_estado_direita = _swap(novo_estado_direita, espaco_idx, 8)
        novo_estado_cima = _swap(novo_estado_cima, espaco_idx, 4)
        
        return [("direita", novo_estado_direita), ("cima", novo_estado_cima), ("esquerda", novo_estado_esquerda)]

    if espaco_idx == 8:
        novo_estado_esquerda = _swap(novo_estado_esquerda, espaco_idx, 7)
        novo_estado_cima = _swap(novo_estado_cima, espaco_idx, 5)
        
        return [("cima", novo_estado_cima), ("esquerda", novo_estado_esquerda)]


def expande(nodo):
    sucessores = sucessor(nodo.estado)
    filhos = [Node(estado, nodo, acao, nodo.custo + 1) for acao, estado in sucessores]

    return filhos


from collections import Counter

def bfs(estado_inicial):
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

        if v.estado == "12345678_":
            solution = []
            while v:
                solution.append(v.acao)
                v = v.pai
            return solution[-2::-1]
        
        if v.estado not in x:
            x.add(v.estado)
            f.extend(expande(v))

    raise ValueError("TILT")