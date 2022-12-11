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
    resultados = pd.DataFrame(columns=["caminho_encontrado", "numero_de_acoes", "tempo_decorrido"])

    estado_inicial = set_estado_inicial()
    for nome_buscador, busca in BUSCADORES_DISPONIVEIS.items():
        inicio = perf_counter()
        caminho_encontrado = busca(estado_inicial)
        tempo_decorrido = perf_counter() - inicio

        resultados.loc[nome_buscador] = {
            "caminho_encontrado": caminho_encontrado,
            "numero_de_acoes": len(caminho_encontrado),
            "tempo_decorrido": tempo_decorrido,
        }

    print(resultados)
