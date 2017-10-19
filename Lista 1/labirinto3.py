from collections import deque

def acha_caminho():
    
    #-----------tratamento das entradas--------------------
    tamanho = input().split()
    n = int(tamanho[0])
    m = int(tamanho[1])
    
    vetor = []
    entrada_portal = None
    saida_portal = None
    
    for i in range(0, n):
        numeros = input().split()
        for j in range(0, m):           
            vetor.append(int(numeros[j]))
            posicao = (i*m)+j
            if vetor[posicao] == 2:
                if entrada_portal == None:
                    entrada_portal = posicao
                else:
                    saida_portal = posicao
    #------------------------------------------------------
                    
    def acha_vizinhos(vertice):
            lista_vizinhos = []

            #canto = 2 vizinhos
            if vertice == 0:
                if (vertice+1 >= 0  and vertice+1 <= (m*n)-1) and vetor[vertice+1] != 1: lista_vizinhos.append(vertice+1)
                if (vertice+m >= 0  and vertice+m <= (m*n)-1) and vetor[vertice+m] != 1: lista_vizinhos.append(vertice+m)
            elif vertice == m-1:
                if (vertice-1 >= 0  and vertice-1 <= (m*n)-1) and vetor[vertice-1] != 1: lista_vizinhos.append(vertice-1)
                if (vertice+m >= 0  and vertice+m <= (m*n)-1) and vetor[vertice+m] != 1: lista_vizinhos.append(vertice+m)
            elif vertice == (m*n) - m:
                if (vertice+1 >= 0  and vertice+1 <= (m*n)-1) and vetor[vertice+1] != 1: lista_vizinhos.append(vertice+1)
                if (vertice-m >= 0  and vertice-m <= (m*n)-1) and vetor[vertice-m] != 1: lista_vizinhos.append(vertice-m)
            elif vertice == (m*n)-1:
                if (vertice-1 >= 0  and vertice-1 <= (m*n)-1) and vetor[vertice-1] != 1: lista_vizinhos.append(vertice-1)
                if (vertice-m >= 0  and vertice-m <= (m*n)-1) and vetor[vertice-m] != 1: lista_vizinhos.append(vertice-m)

            #borda = 3 vizinhos
            elif (vertice >= 1 and vertice < m):
                if (vertice+1 >= 0  and vertice+1 <= (m*n)-1) and vetor[vertice+1] != 1: lista_vizinhos.append(vertice+1)
                if (vertice-1 >= 0  and vertice-1 <= (m*n)-1) and vetor[vertice-1] != 1: lista_vizinhos.append(vertice-1)
                if (vertice+m >= 0  and vertice+m <= (m*n)-1) and vetor[vertice+m] != 1: lista_vizinhos.append(vertice+m)
            elif (vertice % m == 0):
                if (vertice+1 >= 0  and vertice+1 <= (m*n)-1) and vetor[vertice+1] != 1: lista_vizinhos.append(vertice+1)
                if (vertice+m >= 0  and vertice+m <= (m*n)-1) and vetor[vertice+m] != 1: lista_vizinhos.append(vertice+m)
                if (vertice-m >= 0  and vertice-m <= (m*n)-1) and vetor[vertice-m] != 1: lista_vizinhos.append(vertice-m)
            elif ((vertice - (m-1)) % m == 0):
                if (vertice-1 >= 0  and vertice-1 <= (m*n)-1) and vetor[vertice-1] != 1: lista_vizinhos.append(vertice-1)
                if (vertice+m >= 0  and vertice+m <= (m*n)-1) and vetor[vertice+m] != 1: lista_vizinhos.append(vertice+m)
                if (vertice-m >= 0  and vertice-m <= (m*n)-1) and vetor[vertice-m] != 1: lista_vizinhos.append(vertice-m)
            elif (vertice >= (m*n) - m and vertice < (m*n)):
                if (vertice+1 >= 0  and vertice+1 <= (m*n)-1) and vetor[vertice+1] != 1: lista_vizinhos.append(vertice+1)
                if (vertice-1 >= 0  and vertice-1 <= (m*n)-1) and vetor[vertice-1] != 1: lista_vizinhos.append(vertice-1)
                if (vertice-m >= 0  and vertice-m <= (m*n)-1) and vetor[vertice-m] != 1: lista_vizinhos.append(vertice-m)
                                              
            #meio  = 4 vizinhos
            else:
                if (vertice+1 >= 0  and vertice+1 <= (m*n)-1) and vetor[vertice+1] != 1: lista_vizinhos.append(vertice+1)
                if (vertice-1 >= 0  and vertice-1 <= (m*n)-1) and vetor[vertice-1] != 1: lista_vizinhos.append(vertice-1)
                if (vertice+m >= 0  and vertice+m <= (m*n)-1) and vetor[vertice+m] != 1: lista_vizinhos.append(vertice+m)
                if (vertice-m >= 0  and vertice-m <= (m*n)-1) and vetor[vertice-m] != 1: lista_vizinhos.append(vertice-m)

            #-------------caso com portal-----------------
            if vetor[vertice] == 2:
                if vertice == entrada_portal:
                    lista_vizinhos.append(saida_portal)
                else:
                    lista_vizinhos.append(entrada_portal)
            #---------------------------------------------

            print(vertice, lista_vizinhos)      
            return lista_vizinhos

    def busca_largura(raiz, destino):
        fila = deque([raiz])
        pais = {vertice : None for vertice in range(0,(n*m))}
        nivel = {vertice : None for vertice in range(0,(n*m))}

        pais[raiz] = raiz
        nivel[raiz] = 0

        while (len(fila) != 0):
            vertice = fila.popleft()

            #visita ao vértice
            if(vertice == destino):
                print(nivel[destino])
                return

            vizinhos_vertice = acha_vizinhos(vertice)
            for vizinho in vizinhos_vertice:
                if pais[vizinho] == None:
                    fila.append(vizinho)
                    pais[vizinho] = vertice

                    #-------------caso com portal-----------------
                    if vetor[vizinho] == 2 and vetor[vertice] == 2:
                        nivel[vizinho] = nivel[vertice]
                    #---------------------------------------------
                    else:
                        nivel[vizinho] = nivel[vertice] + 1
                    
        if nivel[destino] == None:
            print(-1)

    busca_largura(0, (m*n)-1)
