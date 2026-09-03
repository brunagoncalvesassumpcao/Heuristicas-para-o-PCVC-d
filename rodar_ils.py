

import time
import pathlib
from pathlib import Path
import os

from funcoes_auxiliares import *
from funcoes_auxiliares import custo_total_rota
from ils_funcao import ils

PASTA_PARAMETROS = "info_insercao"
PASTA_RESULTADOS_ILS = "ResultadosILS_insercao"

for nome_arquivo in os.listdir(PASTA_PARAMETROS):
    if(nome_arquivo.endswith(".json")):
        print(f"Aplicando ILS na instância {nome_arquivo}...")
    
        caminho_parametro = Path(PASTA_PARAMETROS) / nome_arquivo
        dados = ler_parametro_json(caminho_parametro)
        
        prioridade_cidade = {
            cidade: i
            for (i, j) in dados["prioridades_dict"].items()
            for cidade in j
        }
        
        inicio_solucao = time.perf_counter()
        caminho_ils = ils(dados["caminho"],  dados["matriz_valores"], prioridade_cidade, dados["d"])
        custo_ils = custo_total_rota(caminho_ils, dados["matriz_valores"])
        fim_solucao = time.perf_counter()
        resultado = {
            "caminhoILS": caminho_ils,
            "custo": custo_ils,
            "tempo": fim_solucao - inicio_solucao,
            "matriz": dados["matriz_valores"],
            "prioridade": prioridade_cidade,
            "d": dados["d"]

        }
        
        caminho_resultado = Path(PASTA_RESULTADOS_ILS) / (nome_arquivo)
        exportar_json(resultado, caminho_resultado)
       
    else:
        continue