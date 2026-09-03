

import time
import pathlib
from pathlib import Path
import os

from funcoes_auxiliares import *
from funcoes_auxiliares import custo_total_rota
from vnd_funcao import VND

PASTA_PARAMETROS = "info_nn"
PASTA_RESULTADOS_VND = "ResultadosVND_nn"

for nome_arquivo in os.listdir(PASTA_PARAMETROS):
    if(nome_arquivo.endswith(".json")):
        print(f"Aplicando VND na instância {nome_arquivo}...")
    
        caminho_parametro = Path(PASTA_PARAMETROS) / nome_arquivo
        dados = ler_parametro_json(caminho_parametro)
        
        prioridade_cidade = {
            cidade: i
            for (i, j) in dados["prioridades_dict"].items()
            for cidade in j
        }
        
        inicio_solucao = time.perf_counter()
        caminho_vnd = VND(dados["caminho"],  dados["matriz_valores"], prioridade_cidade, dados["d"])
        custo_vnd = custo_total_rota(caminho_vnd, dados["matriz_valores"])
        fim_solucao = time.perf_counter()
        resultado = {
            "caminhoVND": caminho_vnd,
            "custo": custo_vnd,
            "tempo": fim_solucao - inicio_solucao,
            "matriz": dados["matriz_valores"],
            "prioridade": prioridade_cidade,
            "d": dados["d"]

        }
        
        caminho_resultado = Path(PASTA_RESULTADOS_VND) / (nome_arquivo)
        exportar_json(resultado, caminho_resultado)
       
    else:
        continue
