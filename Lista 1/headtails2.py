def ordena_strings():
    
    #----------tratamento das entradas---------------------
    global achou
    achou = False
    
    n = int(input())
    strings = []
    for i in range(0,n):
        strings.append(input())

    nao_consta = {string : True for string in strings}
    #------------------------------------------------------
    
    def busca_profundidade():
        for string in strings:
            if achou == False:
                nao_consta.pop(string)
                busca(nao_consta, [string], string)
                nao_consta.update({string : True})
                print(nao_consta)
            else:
                break
            
        if achou == False:
            print(-1)
                    
    def busca(candidato ,estado_atual, pai):
        global achou

        #visita ao vértice
        if len(estado_atual) == n:
            for string in estado_atual:
                print(string)
            achou = True
        else:
            for string in candidato:
                if pai[-1] == string[0]:
                    estado_atual.append(string)
                    print(candidato)
                    busca(candidato, estado_atual, candidato.pop(string))
                    print(candidato)

            candidato.update({estado_atual.pop() : True})
            print(candidato)
                
    busca_profundidade()
