def NN_drelaxada(matriz, d, dic, cidade_inicial=0):
    n = len(matriz)
    visitadas = [False] * n
    caminho = [cidade_inicial]
    cidade_atual = cidade_inicial
    visitadas[cidade_atual] = True
    prioridades_ativas = []

    for _ in range(n - 1):
        prioridades_ativas = [dic[i] for i in range(n) if not visitadas[i]]
        if not prioridades_ativas:
            break

        maior_prioridade_atual = min(prioridades_ativas)

        proxima_cidade = None
        menor_distancia = float('inf')


        for cidade in range(n):
            if dic[cidade] > maior_prioridade_atual + d:
                continue    

            if not visitadas[cidade] and matriz[cidade_atual][cidade] < menor_distancia:
                menor_distancia = matriz[cidade_atual][cidade]
                proxima_cidade = cidade

        if proxima_cidade is None:
            continue

        caminho.append(proxima_cidade)
        visitadas[proxima_cidade] = True
        cidade_atual = proxima_cidade


    caminho.append(cidade_inicial)

    return caminho

def custo_total_rota(rota, matriz_distancia):
    return sum(
        matriz_distancia[rota[i]][rota[i+1]]
        for i in range(len(rota) - 1)
    )


