import random
from collections import Counter
from funcoes_auxiliares import custo_total_rota

def viavel(rota, P, d):

    total_por_prioridade = Counter(P.values())

    
    visitados = Counter()

    prioridade_concluida = 0

    for cidade in rota:

        p = P[cidade]

        
        if p > prioridade_concluida + d:
            return False

        visitados[p] += 1

        
        while (
            prioridade_concluida in total_por_prioridade and
            visitados[prioridade_concluida] == total_por_prioridade[prioridade_concluida]
        ):
            prioridade_concluida += 1

    return True


def relocate1(rota, matriz, P, valord):

    melhor_rota = rota[1:-1]
    melhor_custo = custo_total_rota(rota, matriz)

    for i in range(len(melhor_rota)):

        for j in range(len(melhor_rota)):

            if i == j:
                continue

            rotavnd = melhor_rota.copy()

            v = rotavnd.pop(i)
            rotavnd.insert(j, v)

            if viavel([0] + rotavnd + [0], P, valord):

                custo = custo_total_rota([0] + rotavnd + [0], matriz)

                if custo < melhor_custo:
                    melhor_custo = custo
                    melhor_rota = rotavnd

    return [0] + melhor_rota + [0]



def relocate2(rota, matriz, P, valord):

    melhor_rota = rota[1:-1]
    melhor_custo = custo_total_rota(rota, matriz)
    n = len(melhor_rota)

    for i in range(n - 1):

        if P[melhor_rota[i]] != P[melhor_rota[i+1]]:
            continue

        for j in range(n):

            rotavnd = melhor_rota.copy()

            u = rotavnd.pop(i)
            v = rotavnd.pop(i)

            rotavnd.insert(j, u)
            rotavnd.insert(j+1, v)

            if viavel([0] + rotavnd + [0], P, valord):

                custo = custo_total_rota([0] + rotavnd + [0], matriz)

                if custo < melhor_custo:
                    melhor_custo = custo
                    melhor_rota = rotavnd

    return [0] + melhor_rota + [0]



def swap11(rota, matriz, P, d):

    melhor_rota = rota[1:-1]
    melhor_custo = custo_total_rota(rota, matriz)
    n = len(melhor_rota)

    for i in range(n):

        for j in range(i+1, n):

            rotavnd = melhor_rota.copy()

            rotavnd[i], rotavnd[j] = rotavnd[j], rotavnd[i]

            if viavel([0] + rotavnd + [0], P, d):

                custo = custo_total_rota([0] + rotavnd + [0], matriz)

                if custo < melhor_custo:
                    melhor_custo = custo
                    melhor_rota = rotavnd

    return [0] + melhor_rota + [0]



def swap22(rota, matriz, P, valord):

    melhor_rota = rota[1:-1]
    melhor_custo = custo_total_rota(rota, matriz)
    n = len(melhor_rota)

    for i in range(n - 1):

        for j in range(i+2, n - 1):

            if abs(i-j) <= 1:
                continue

            rotavnd = melhor_rota.copy()

            rotavnd[i:i+2], rotavnd[j:j+2] = rotavnd[j:j+2], rotavnd[i:i+2]

            if viavel([0] + rotavnd + [0], P, valord):

                custo = custo_total_rota([0] + rotavnd + [0], matriz)

                if custo < melhor_custo:
                    melhor_custo = custo
                    melhor_rota = rotavnd

    return [0] + melhor_rota + [0]


def swap21(rota, matriz, P, valord):

    melhor_rota = rota[1:-1]
    melhor_custo = custo_total_rota(rota, matriz)

    n = len(melhor_rota)   

    for i in range(n - 1):      

        for j in range(n):      

            if j == i or j == i + 1:
                continue

            rotavnd = melhor_rota.copy()

            
            if i < j:

                u = rotavnd.pop(i)
                v = rotavnd.pop(i)

                w = rotavnd.pop(j - 2)

                rotavnd.insert(i, w)
                rotavnd.insert(j - 1, u)
                rotavnd.insert(j, v)

            else:

                w = rotavnd.pop(j)

                u = rotavnd.pop(i - 1)
                v = rotavnd.pop(i - 1)

                rotavnd.insert(j, u)
                rotavnd.insert(j + 1, v)
                rotavnd.insert(i, w)

            if viavel([0] + rotavnd + [0], P, valord):

                custo = custo_total_rota([0] + rotavnd + [0], matriz)

                if custo < melhor_custo:
                    melhor_custo = custo
                    melhor_rota = rotavnd

    return [0] + melhor_rota + [0]