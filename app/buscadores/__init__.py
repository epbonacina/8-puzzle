from buscadores.bfs import bfs
from buscadores.dfs import dfs
from buscadores.a_estrela import a_estrela_manhattan, a_estrela_hamming

BUSCADORES_DISPONIVEIS = {
    "BFS": bfs,
    "DFS": dfs,
    "A_ESTRELA_HAMMING": a_estrela_hamming,
    "A_ESTRELA_MANHATTAN": a_estrela_manhattan,
}

__all__ = BUSCADORES_DISPONIVEIS