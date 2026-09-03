import os
import json
from funcoes_auxiliares import viavel


def verificar_instancias(pasta):

    for nome_arquivo in os.listdir(pasta):

        caminho_arquivo = os.path.join(pasta, nome_arquivo)

        if not os.path.isfile(caminho_arquivo):
            continue

        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)

        rota = dados["caminho"]

       
        prioridade = {}

        for p, vertices in dados["prioridades_dict"].items():
            p = int(p)
            for v in vertices:
                prioridade[v] = p

        d = dados["d"]

        erros = []

        if rota[0] != 0 or rota[-1] != 0:
            erros.append("Primeiro ou último elemento não é 0.")

       
        if any(v == 0 for v in rota[1:-1]):
            erros.append("Existe um zero no meio da rota.")

       
        miolo = rota[1:-1]

        if len(miolo) != len(set(miolo)):
            repetidos = [v for v in set(miolo) if miolo.count(v) > 1]
            erros.append(f"Vértices repetidos: {repetidos}")

      
        if not viavel(rota, prioridade, d):
            erros.append("A rota viola a regra d-relaxada.")


       
        if erros:
            print(f"\n{nome_arquivo}")
            for erro in erros:
                print(f"  - {erro}")
        else:
            print(f"{nome_arquivo}: OK")



PASTA = "saida"

verificar_instancias(PASTA)