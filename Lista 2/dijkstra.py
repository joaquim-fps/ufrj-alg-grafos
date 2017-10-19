def get_graph():
    # graph['vertices'] := conjunto de vértices do grafo
    # graph['adjacent'] := lista de adjacência do grafo
    # Peso da aresta é guardado numa tupla: (vertice_adjacente, peso)
    graph = {'vertices': set(), 'adjacent': {}}

    size  = input().split()
    num_v = int(size[0])
    num_e = int(size[1])

    for i in range(0, num_e):
        edge   = input().split()
        weight = int(edge[2])

        graph['vertices'].update(edge)

        adj1 = graph['adjacent'].get(edge[0],[])
        adj1.append([edge[1],weight])
        graph['adjacent'].update({edge[0]:adj1})

        adj2 = graph['adjacent'].get(edge[1],[])
        adj2.append([edge[0],weight])
        graph['adjacent'].update({edge[1]:adj2})

    return graph

def get_source(graph):
    while(True):
        source = input()
        
        if source in graph['vertices']:
            return source

def get_destination(graph):
    while(True):
        destination = input()

        if destination in graph['vertices']:
            return destination

def dijkstra(graph, source):
    import math
    from heapq import heappop, heappush

    adjancecy_list   = graph['adjacent']

    distance         = {v : math.inf for v in graph['vertices']}
    ancestor         = {v : None for v in graph['vertices']}

    distance[source] = 0
    ancestor[source] = source

    queue            = [(distance[source], source)]
    seen             = set()

    while len(queue) != 0:
        current_vertice = heappop(queue)[1]

        seen.add(current_vertice)

        for neighboor in adjancecy_list[current_vertice]:
            neighboor_vertice = neighboor[0]
            edge_weight       = neighboor[1]

            # Se vizinho ainda não foi "visto", relaxe a aresta (vertice, vizinho)
            if (neighboor_vertice not in seen) and (distance[neighboor_vertice] > (distance[current_vertice] + edge_weight)):
                distance[neighboor_vertice] = distance[current_vertice] + edge_weight
                ancestor[neighboor_vertice] = current_vertice

                heappush(queue, (distance[neighboor_vertice], neighboor_vertice))
                
    return ancestor, distance

def generate_path(graph, source, destination):
    ancestor, distance = dijkstra(graph, source)

    destination_path        = [destination]
    destination_path_weight = distance[destination]

    while destination != source:
        destination_path.append(ancestor[destination])
        destination = ancestor[destination]

    destination_path.reverse()

    return {'path': destination_path, 'weight': destination_path_weight}

def shortest_path():
    graph       = get_graph()
    source      = get_source(graph)
    destination = get_destination(graph)

    return generate_path(graph, source, destination)

# 3) Se existe um ciclo onde todas as arestas tem peso negativo,
# então podemos percorrer este ciclo quantas vezes quisermos, 
# reduzindo o custo de qualquer caminho que ele faça parte, infinitamente.
# Dito isso, o algoritmo de Dijkstra não funciona com arestas de peso negativo,
# visto que essas arestas podem diminuir o custo de vértices que já foram
# considerados como "vistos" e fariam o algoritmo errar. Existem alternativas
# para arestas de peso negativo, como o algoritmo de Bellman-Ford.
