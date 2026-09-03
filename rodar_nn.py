#!/usr/bin/env python3

import time
import pathlib
from pathlib import Path
import os

from funcoes_auxiliares import *
from nn_d_relaxado import NN_drelaxada, custo_total_rota

PASTA_INSTANCIAS = "Instancias"
PASTA_RESULTADOS = "Resultados"

for nome_arquivo in os.listdir(PASTA_INSTANCIAS):
    if(nome_arquivo.endswith(".htsp")):
        print(f"Aplicando inserção na instância {nome_arquivo}...")
    
        caminho_instancia = Path(PASTA_INSTANCIAS) / nome_arquivo
        dados = ler_instancia(caminho_instancia)
        
        prioridade_cidade = {
            cidade: i
            for (i, j) in dados["prioridades_dict"].items()
            for cidade in j
        }
        
        inicio_solucao = time.perf_counter()
        caminho = NN_drelaxada(dados["matriz_valores"], dados["d"], prioridade_cidade)
        custo = custo_total_rota(caminho, dados["matriz_valores"])
        fim_solucao = time.perf_counter()
        resultado = {
            "caminho": caminho,
            "custo": custo,
            "tempo": fim_solucao - inicio_solucao
        }
        
        caminho_resultado = Path(PASTA_RESULTADOS) / (nome_arquivo.removesuffix(".htsp") + ".json")
        exportar_json(resultado, caminho_resultado)
       
    else:
        continue
