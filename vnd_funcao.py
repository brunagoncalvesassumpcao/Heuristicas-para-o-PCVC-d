from estruturas_vizinhança import relocate1, relocate2, swap11, swap22, swap21, viavel
from funcoes_auxiliares import custo_total_rota

def VND(rota, matriz, P, d):

    melhor_rota = rota.copy()
    melhor_custo = custo_total_rota(melhor_rota, matriz)

    estruturas = [
        relocate1,
        relocate2,
        swap11,
        swap22,
        swap21
    ]

    k = 0

    while k < len(estruturas):

        vizinho = estruturas[k](melhor_rota, matriz, P, d)

        custo_vizinho = custo_total_rota(vizinho, matriz)

        if custo_vizinho < melhor_custo:

            melhor_rota = vizinho
            melhor_custo = custo_vizinho

            
            k = 0

        else:

            
            k += 1

    return melhor_rota



