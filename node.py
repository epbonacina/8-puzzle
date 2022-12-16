from acao import Acao


def swap(string, i, j):
    ls = list(string)
    ls[i], ls[j] = ls[j], ls[i]
    return ''.join(ls)


class Node:
    def __init__(self, estado, custo, acao=None, pai=None):
        self.estado = estado
        self.pai = pai
        self.acao = acao
        self.custo = custo

    def sucessor(self):
        iblank = self.estado.index("_")
        succ = []

        if iblank > 2:
            iup = iblank-3
            n_state = swap(self.estado, iblank, iup)
            succ.append((Acao.acima, n_state))

        if iblank < 6:
            idown = iblank+3
            n_state = swap(self.estado, iblank, idown)
            succ.append((Acao.abaixo, n_state))

        if iblank % 3 != 0:
            ileft = iblank - 1
            n_state = swap(self.estado, iblank, ileft)
            succ.append((Acao.esquerda, n_state))

        if iblank % 3 != 2:
            iright = iblank + 1
            n_state = swap(self.estado, iblank, iright)
            succ.append((Acao.direita, n_state))

        return succ

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

    def expand(self):
        succ = self.sucessor()
        expansion = []
        for action, state in succ:
            expansion.append(Node(state, self.custo+1, action, self))
        return expansion

    def trace_history(self):
        trace = []
        v = self
        while v:
            trace.append(v.acao.name)
            v = v.pai
        return trace[-2::-1]
