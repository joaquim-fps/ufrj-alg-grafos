def get_graph():
    # graph['vertices'] := conjunto de vértices do grafo
    # graph['adjacent'] := lista de adjacência do grafo
    graph = {'vertices': set(), 'adjacent': {}}

    size  = input().split()
    num_v = int(size[0])
    num_e = int(size[1])

    for i in range(0, num_e):
        edge = input().split()
        graph['vertices'].update(edge)

        adj1 = graph['adjacent'].get(edge[0],[])
        adj1.append(edge[1])
        graph['adjacent'].update({edge[0]:adj1})

        adj2 = graph['adjacent'].get(edge[1],[])
        adj2.append(edge[0])
        graph['adjacent'].update({edge[1]:adj2})

    return graph

def get_root(graph):
    # Um vértice qualquer do grafo
    for vertice in graph['vertices']:
        return vertice

def format_edges(edges):
        formatted_edges = []

        for edge1, edge2 in edges:
            formatted_edges.append("(" + str(edge1) + "," + str(edge2) + ")")

        return formatted_edges

def DFS(graph, root):
    global entrance
    global root_children
    
    bridge_edges   = []
    adjacency_list = graph['adjacent']
    
    bridge_vertice = {v : False for v in graph['vertices']}
    parent         = {v : None for v in graph['vertices']}
    entrance_order = {v : 0 for v in graph['vertices']}
    low            = {v : 0 for v in graph['vertices']}

    entrance       = 1
    parent[root]   = root
    root_children  = 0

    def search(graph, vertice):
        global entrance
        global root_children
        
        entrance_order[vertice] = entrance
        low[vertice]            = entrance_order[vertice]
        entrance                = entrance + 1
        
        for neighboor in adjacency_list[vertice]:
            if parent[neighboor] == None:
                parent[neighboor] = vertice

                if vertice == root: 
                    root_children = root_children + 1
                
                search(graph, neighboor)

                if low[neighboor] < low[vertice]:
                    low[vertice]  = low[neighboor]

                if bridge_vertice[neighboor]:
                    bridge_edges.append([vertice,neighboor])
                    
            elif neighboor != parent[vertice] and entrance_order[neighboor] < low[vertice]:
                low[vertice] = entrance_order[neighboor]

        # Se low[v] = v, então v está conectado por uma ponte ao seu pai
        if low[vertice] == entrance_order[vertice]:
            bridge_vertice[vertice] = True

    search(graph, root)

    return bridge_edges

def bridges():
    graph        = get_graph()
    root         = get_root(graph)

    bridge_edges = DFS(graph, root)
    
    return format_edges(bridge_edges)
