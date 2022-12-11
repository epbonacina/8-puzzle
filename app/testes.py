from time import perf_counter
import pandas as pd

from buscadores import BUSCADORES_DISPONIVEIS


resultados = pd.DataFrame(columns=["resultado", "tempo_decorrido"])
for nome_buscador, busca in BUSCADORES_DISPONIVEIS.items():
    inicio = perf_counter()
    resultado = busca("2_3541687")
    tempo_decorrido = perf_counter() - inicio

    resultados.loc[nome_buscador] = {"resultado": resultado, "tempo_decorrido": tempo_decorrido}

print(resultados)