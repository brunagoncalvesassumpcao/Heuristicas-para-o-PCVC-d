import os
import json
from pathlib import Path

from funcoes_auxiliares import ler_instancia, ler_json, exportar_json

pasta_htsp = "Instancias"
pasta_json = "Resultados_insercao"
pasta_saida = "saida"

os.makedirs(pasta_saida, exist_ok=True)

for arquivo in os.listdir(pasta_htsp):

    if not arquivo.endswith(".htsp"):
        continue

    nome = os.path.splitext(arquivo)[0]

    caminho_htsp = os.path.join(pasta_htsp, nome + ".htsp")
    caminho_json = os.path.join(pasta_json, nome + ".json")

    if not os.path.exists(caminho_json):
        print(f"{nome} não possui arquivo json correspondente.")
        continue

    dados = ler_instancia(caminho_htsp)

    dados_json = ler_json(caminho_json)

    dados.update(dados_json)

    
    caminho_resultado = Path(pasta_saida) / (nome.removesuffix(".htsp") + ".json")
    exportar_json(dados, caminho_resultado)