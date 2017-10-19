def transforma(matriz, n):      
    lista = []
    vizinhos = []

    for i in range(0, n):
        for j in range(0, n):
            if matriz[i][j] == 1:
                vizinhos.append(j+1) #Vértices numerados de 1 a N
        
        lista.append(vizinhos.copy())
        vizinhos.clear()

    return lista


