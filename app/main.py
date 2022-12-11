import os
from time import sleep, perf_counter
import pandas as pd

from buscadores import BUSCADORES_DISPONIVEIS


def set_estado_inicial():
    while True:
        estado_inicial = input("Digite o estado inicial: ")
        os.system("cls")
        if len(set(estado_inicial)) != 9:
            print("Estado inicial inválido")
        else:
            break
    return estado_inicial


if __name__ == "__main__":
    resultados = pd.DataFrame(
        columns=[
            "caminho_encontrado", 
            "nodos_explorados",
            "custo",
            "tempo_decorrido",
        ]
    )

    estado_inicial = set_estado_inicial()
    for nome_buscador, busca in BUSCADORES_DISPONIVEIS.items():
        inicio = perf_counter()
        nodos_explorados, caminho_encontrado = busca(estado_inicial)
        tempo_decorrido = perf_counter() - inicio

        resultados.loc[nome_buscador] = {
            "caminho_encontrado": caminho_encontrado,
            "nodos_explorados": nodos_explorados,
            "custo": len(caminho_encontrado) if caminho_encontrado else None,
            "tempo_decorrido": tempo_decorrido,
        }

    print(resultados)
