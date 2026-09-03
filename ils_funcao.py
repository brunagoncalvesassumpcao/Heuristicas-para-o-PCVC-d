import numpy
import random
import copy
from vnd_funcao import VND
from funcoes_auxiliares import custo_total_rota



def perturbar(s, P, d):
    s_inicial = s[1:-1]  

    i = random.randrange(len(s_inicial))
    
    vertice = s_inicial.pop(i)

    permitidas = {i: v for i, v in enumerate(s_inicial) if P[vertice] - d <= P[v] <= P[vertice] + d}

    j = random.choice(list(permitidas.keys()))
    
    s_inicial.insert(j, vertice)
    
    return [0] + s_inicial + [0]


def busca_local(rota, matriz, P, d):
    return VND(rota, matriz, P, d)




def ils(solucao_inicial, matriz, P, d, max_iter=5):
 
    s = busca_local(copy.deepcopy(solucao_inicial), matriz, P, d)

    melhor = copy.deepcopy(s)
    melhor_custo = custo_total_rota(melhor, matriz)

    for _ in range(max_iter):

        
        s_linha = perturbar(copy.deepcopy(s), P, d)

       
        s_linha = busca_local(s_linha, matriz, P, d)

        
        if custo_total_rota(s_linha, matriz) < custo_total_rota(s, matriz):
            s = copy.deepcopy(s_linha)

        if custo_total_rota(s, matriz) < melhor_custo:
            melhor = copy.deepcopy(s)
            melhor_custo = custo_total_rota(s, matriz)

    return melhor