import numpy as np



#Função que encontra o vértice mais distante da rota
def maisdistantedarota(matriz_custo, rota, nao_visitados):
    melhor_vertice = None
    maior_distancia = -float('inf')

    for u in nao_visitados:
        menor_distancia = float('inf')
        for v in rota:
            if matriz_custo[u][v] < menor_distancia:
                menor_distancia = matriz_custo[u][v]
        if menor_distancia > maior_distancia:
            maior_distancia = menor_distancia
            melhor_vertice = u
    return melhor_vertice


#Função que encontra a posição mínima para inserção dos vértices
def posicao_limite(prioridade_anterior, rota, prioridade):
    menor_posicao = None

    for posicao, vetor in enumerate(rota[:-1]):
        if prioridade[vetor] == prioridade_anterior:
            menor_posicao = posicao
    return menor_posicao




def insercao(matriz, d, prioridade, c0 = 0):
    n = len(matriz)
    caminho = [0]
    vertices_nao_visitados = [i for i in range(n) if i not in caminho]
    maior_prioridade_atual = min(prioridade[v] for v in vertices_nao_visitados)
    candidatos = []

    for v in vertices_nao_visitados:
        if prioridade[v] <= maior_prioridade_atual + d:
            candidatos.append(v)
    
    

    v_mais_distante_de_c0 = maisdistantedarota(matriz, caminho, candidatos)

    caminho = [0, v_mais_distante_de_c0, 0]
    vertices_nao_visitados = [i for i in range(n) if i not in caminho]
    vertices_visitados = caminho[:-1]

    prioridade_anterior = 0

    while vertices_nao_visitados:
        maior_prioridade_atual = min(prioridade[v] for v in vertices_nao_visitados)
        

        lista = []
        for v in vertices_nao_visitados:
            if prioridade[v] <= maior_prioridade_atual + d:
                lista.append(v)

        
        
        vertice_escolhido = maisdistantedarota(matriz, caminho, lista)
        

        if prioridade_anterior + 1 == maior_prioridade_atual:
            pos_limite = posicao_limite(prioridade_anterior, caminho, prioridade)

        if prioridade_anterior != maior_prioridade_atual and prioridade_anterior + 1 != maior_prioridade_atual:
            
            pos_limite_penultimo = posicao_limite(prioridade_anterior, caminho, prioridade)
            pos_limite_ultimo = posicao_limite(prioridade_anterior + 1, caminho, prioridade)
            if pos_limite_ultimo > pos_limite_penultimo:
                pos_limite = pos_limite_ultimo
            else: pos_limite = pos_limite_penultimo

             
        
        melhor_custo = float('inf')
        melhor_posicao = None
        for i in range(pos_limite, len(caminho) - 1):
            vi = caminho[i]
            vj = caminho[i+1]

            custo = (
                matriz[vi][vertice_escolhido] + 
                matriz[vertice_escolhido][vj] - 
                matriz[vi][vj]
            )

            if custo < melhor_custo:
                melhor_custo = custo
                melhor_posicao = i + 1

    

        if melhor_posicao == None:
            caminho.insert(pos_limite, vertice_escolhido)
            
                   
        else:
            caminho.insert(melhor_posicao, vertice_escolhido)
                
        
        vertices_visitados = caminho[:-1]
        vertices_nao_visitados.remove(vertice_escolhido)
        prioridade_anterior = maior_prioridade_atual

        
            
    return caminho



