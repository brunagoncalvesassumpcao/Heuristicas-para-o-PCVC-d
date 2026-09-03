import re
import json

def ler_instancia(caminho: str) -> dict[str, int | list[list[int]] | dict[int, list[int]]]:
    with open(caminho, "r") as file:
        linha = file.readline().strip()
        quantidade_pontos = int(linha)

        linha = file.readline().strip()

        padrao_int = re.compile(r"\d+")
        quantidade_grupos_prioridade, d =  [
            int(i.group()) for i in padrao_int.finditer(linha)
        ]
        
        matriz_valores = list()
        prioridades_dict = dict()

        for _ in range(quantidade_pontos):
            linha = file.readline().strip()
            
            matriz_valores.append([
                int(i.group()) for i in padrao_int.finditer(linha)
            ])

        for _ in range(quantidade_grupos_prioridade):
            linha = file.readline().strip()
            
            valores = [int(i.group()) for i in padrao_int.finditer(linha)]
            
            prioridades_dict[valores[0]] = [i-1 for i in valores[2:]]

    return {
        "quantidade_pontos": quantidade_pontos,
        "d": d,
        "matriz_valores": matriz_valores,
        "prioridades_dict": prioridades_dict
    }

def ler_json(caminho: str) -> dict:
    return json.load(open(caminho, "r"))

def exportar_json(dicionario: dict, caminho: str) -> None:
    json.dump(dicionario, open(caminho, "w"))
    
    return




def ler_parametro_json(caminho: str) -> dict[
    str,
    int | float | list[int] | list[list[int]] | dict[int, list[int]]
]:
    with open(caminho, "r", encoding="utf-8") as file:
        dados = json.load(file)

    # As chaves do JSON são strings. Converte para inteiros.
    dados["prioridades_dict"] = {
        int(chave): valor
        for chave, valor in dados["prioridades_dict"].items()
    }

    return {
        "quantidade_pontos": dados["quantidade_pontos"],
        "d": dados["d"],
        "matriz_valores": dados["matriz_valores"],
        "prioridades_dict": dados["prioridades_dict"],
        "caminho": dados["caminho"],
        "custo": dados["custo"],
        "tempo": dados["tempo"],
    }


def custo_total_rota(rota, matriz_distancia):
    return sum(
        matriz_distancia[rota[i]][rota[i+1]]
        for i in range(len(rota) - 1)
    )