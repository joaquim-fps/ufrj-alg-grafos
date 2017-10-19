def acha_caminho():
    
    #-------------------tratamento das entradas-----------------------
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
    #-----------------------------------------------------------------

    def converte_matriz(matriz):
        adjacencia = [[0 for l in range (n*m)] for k in range(0, (n*m))]

        for i in range(0, (n*m)):
            if vetor[i] == 1:
                continue

            vizinhos_vertice = acha_vizinhos(i)
            #---------------------caso com portal------------------------
            if vetor[i] == 2:
                if i == entrada_portal:
                    vizinhos_vertice += acha_vizinhos(saida_portal)
                else:
                    vizinhos_vertice += acha_vizinhos(entrada_portal)
            #------------------------------------------------------------

            for vizinho in vizinhos_vertice:
                aux = vetor[vizinho]
                
                if aux == 1:
                    adjacencia[i][vizinho] = 0
                else:
                    adjacencia[i][vizinho] = 1            

        return adjacencia

    def acha_vizinhos(position):
        lista_vizinhos = []

        #canto = 2 vizinhos
        if position == 0:
            if (position+1 >= 0  and position+1 <= (m*n)-1) and vetor[position+1] != 1: lista_vizinhos.append(position+1)
            if (position+m >= 0  and position+m <= (m*n)-1) and vetor[position+m] != 1: lista_vizinhos.append(position+m)
        elif position == m-1:
            if (position-1 >= 0  and position-1 <= (m*n)-1) and vetor[position-1] != 1: lista_vizinhos.append(position-1)
            if (position+m >= 0  and position+m <= (m*n)-1) and vetor[position+m] != 1: lista_vizinhos.append(position+m)
        elif position == (m*n) - m:
            if (position+1 >= 0  and position+1 <= (m*n)-1) and vetor[position+1] != 1: lista_vizinhos.append(position+1)
            if (position-m >= 0  and position-m <= (m*n)-1) and vetor[position-m] != 1: lista_vizinhos.append(position-m)
        elif position == (m*n)-1:
            if (position-1 >= 0  and position-1 <= (m*n)-1) and vetor[position-1] != 1: lista_vizinhos.append(position-1)
            if (position-m >= 0  and position-m <= (m*n)-1) and vetor[position-m] != 1: lista_vizinhos.append(position-m)

        #borda = 3 vizinhos
        elif (position >= 1 and position < m):
            if (position+1 >= 0  and position+1 <= (m*n)-1) and vetor[position+1] != 1: lista_vizinhos.append(position+1)
            if (position-1 >= 0  and position-1 <= (m*n)-1) and vetor[position-1] != 1: lista_vizinhos.append(position-1)
            if (position+m >= 0  and position+m <= (m*n)-1) and vetor[position+m] != 1: lista_vizinhos.append(position+m)
        elif (position % m == 0):
            if (position+1 >= 0  and position+1 <= (m*n)-1) and vetor[position+1] != 1: lista_vizinhos.append(position+1)
            if (position+m >= 0  and position+m <= (m*n)-1) and vetor[position+m] != 1: lista_vizinhos.append(position+m)
            if (position-m >= 0  and position-m <= (m*n)-1) and vetor[position-m] != 1: lista_vizinhos.append(position-m)
        elif ((position - (m-1)) % m == 0):
            if (position-1 >= 0  and position-1 <= (m*n)-1) and vetor[position-1] != 1: lista_vizinhos.append(position-1)
            if (position+m >= 0  and position+m <= (m*n)-1) and vetor[position+m] != 1: lista_vizinhos.append(position+m)
            if (position-m >= 0  and position-m <= (m*n)-1) and vetor[position-m] != 1: lista_vizinhos.append(position-m)
        elif (position >= (m*n) - m and position < (m*n)):
            if (position+1 >= 0  and position+1 <= (m*n)-1) and vetor[position+1] != 1: lista_vizinhos.append(position+1)
            if (position-1 >= 0  and position-1 <= (m*n)-1) and vetor[position-1] != 1: lista_vizinhos.append(position-1)
            if (position-m >= 0  and position-m <= (m*n)-1) and vetor[position-m] != 1: lista_vizinhos.append(position-m)
                                          
        #meio  = 4 vizinhos
        else:
            if (position+1 >= 0  and position+1 <= (m*n)-1) and vetor[position+1] != 1: lista_vizinhos.append(position+1)
            if (position-1 >= 0  and position-1 <= (m*n)-1) and vetor[position-1] != 1: lista_vizinhos.append(position-1)
            if (position+m >= 0  and position+m <= (m*n)-1) and vetor[position+m] != 1: lista_vizinhos.append(position+m)
            if (position-m >= 0  and position-m <= (m*n)-1) and vetor[position-m] != 1: lista_vizinhos.append(position-m)

        return lista_vizinhos

    def matrixmult (A, B):
        rows_A = len(A)
        cols_A = len(A[0])
        rows_B = len(B)
        cols_B = len(B[0])

        if cols_A != rows_B:
            print ("Cannot multiply the two matrices. Incorrect dimensions.")
            return

        C = [[0 for row in range(cols_B)] for col in range(rows_A)]

        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    C[i][j] += A[i][k] * B[k][j]
        return C

    #---------------main--------------------
    matriz_adjacente = converte_matriz(vetor)

    k = 1
    produtorio = matriz_adjacente
    while (produtorio[0][(n*m)-1] < 1 and ((k <= ((m*n)+n)/2) or (k <= ((m*n)+n+(2*m)-2)/2) or (k <= ((m*n)+m)/2) or (k <= ((m*n)+m+(2*n)-2)/2))):
        produtorio = matrixmult(produtorio, matriz_adjacente)
        k += 1

    if produtorio[0][(n*m)-1] >= 1:
        print(k)
    else:
        print(-1)
    #----------------------------------------

    

