from utils import Queue, Stack, AStar, MANHATTAN_DICT


def swap(string, i, j):
    ls = list(string)
    ls[i], ls[j] = ls[j], ls[i]
    return ''.join(ls)


class Nodo:
    def __init__(self, estado, pai=None, acao=None, custo=0):
        self.estado = estado
        self.custo = custo or 0
        self.acao = acao
        self.pai = pai

    def trace_history(self):
        trace = []
        v = self
        while v:
            trace.append(v.acao)
            v = v.pai
        return trace[-2::-1]

    def __lt__(self, other):
        return self.custo < other.custo

    def __le__(self, other):
        return self.custo <= other.custo

    def __eq__(self, other):
        return self.custo == other.custo

    def __gt__(self, other):
        return self.custo > other.custo

    def __ge__(self, other):
        return self.custo >= other.custo

    def __ne__(self, other):
        return self.custo != other.custo


def sucessor(estado):
    iblank = estado.index("_")
    succ = []

    if iblank > 2:
        iup = iblank-3
        n_state = swap(estado, iblank, iup)
        succ.append(("acima", n_state))

    if iblank < 6:
        idown = iblank+3
        n_state = swap(estado, iblank, idown)
        succ.append(("abaixo", n_state))

    if iblank % 3 != 2:
        iright = iblank + 1
        n_state = swap(estado, iblank, iright)
        succ.append(("direita", n_state))

    if iblank % 3 != 0:
        ileft = iblank - 1
        n_state = swap(estado, iblank, ileft)
        succ.append(("esquerda", n_state))

    return succ


def expande(nodo):
    succ = sucessor(nodo.estado)
    expansion = []
    for action, state in succ:
        expansion.append(Nodo(state, nodo, action, nodo.custo+1))
    return expansion


def bfs(estado_inicial):
    return busca_grafo(estado_inicial, Queue())


def dfs(estado_inicial):
    return busca_grafo(estado_inicial, Stack())


def hamming_heuristic(item):
    goal = "12345678_"
    state = item.estado
    sum = 0
    for i, v in enumerate(goal):
        if v != state[i]:
            sum += 1
    return sum


def astar_hamming(estado_inicial):
    return busca_grafo(estado_inicial, AStar(hamming_heuristic))


def manhattan_heuristic(item):
    state = item.estado
    total = 0
    for i, v in enumerate(state):
        total += MANHATTAN_DICT[str(i)][v]
    return total


def astar_manhattan(estado_inicial):
    return busca_grafo(estado_inicial, AStar(manhattan_heuristic))


X = None
def busca_grafo(estado_inicial, F):
    objective = "12345678_"
    global X
    X = set()
    F.insert(Nodo(estado_inicial))
    while True:
        if F.empty():
            return None
        v = F.pop()
        if v.estado == objective:
            return v.trace_history()
        if v.estado not in X:
            X.add(v.estado)
            for node in expande(v):
                F.insert(node)
                