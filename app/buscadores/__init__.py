from buscadores.bfs import bfs
from buscadores.dfs import dfs
from buscadores.a_estrela_manhattan import a_estrela_manhattan
from buscadores.a_estrela_hamming import a_estrela_hamming

BUSCADORES_DISPONIVEIS = {
    "BFS": bfs,
    "DFS": dfs,
    "A_ESTRELA_MANHATTAN": a_estrela_manhattan,
    "A_ESTRELA_HAMMING": a_estrela_hamming,
}

__all__ = BUSCADORES_DISPONIVEIS