import os
from time import perf_counter
import pandas as pd

import solucao

BUSCADORES_DISPONIVEIS = {
    "bfs": solucao.bfs,
    "dfs": solucao.dfs,
    "astar_hamming": solucao.astar_hamming,
    "astar_manhattan": solucao.astar_manhattan,
}


def set_estado_inicial():
    while True:
        estado_inicial = input("Type the initial state: ")
        os.system("cls")
        if len(set(estado_inicial)) != 9:
            print("Invalid initial state")
        else:
            break
    return estado_inicial


if __name__ == "__main__":
    resultados = pd.DataFrame(
        columns=[
            "explored_nodes",
            "cost",
            "elapsed_time",
        ]
    )

    estado_inicial = set_estado_inicial()
    for nome_buscador, busca in BUSCADORES_DISPONIVEIS.items():
        inicio = perf_counter()
        caminho_encontrado = busca(estado_inicial)
        tempo_decorrido = perf_counter() - inicio

        resultados.loc[nome_buscador] = {
            "explored_nodes": len(solucao.X),
            "cost": len(caminho_encontrado) if caminho_encontrado else None,
            "elapsed_time": tempo_decorrido,
        }

    print(resultados)
