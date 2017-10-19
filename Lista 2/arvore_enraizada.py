from collections import deque
import math

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

def format_tree(tree):
    parent = tree[0]
    order  = tree[1]
    
    # Formato := Pai : [filhos]
    formatted_tree = {v : [] for v in parent.keys()}
    formatted_tree['root'] = min(order, key=order.get)

    while(len(order) != 0):
        vertice = min(order, key=order.get)
        order.pop(vertice)

        for node in parent.items():
            parent_v = node[1]
            child_v  = node[0]
            
            if parent_v == vertice and parent_v != child_v:
                formatted_tree[parent_v].append(child_v)

    return formatted_tree

def BFS(graph, root):
    queue          = deque([root])
    adjacency_list = graph['adjacent']

    parent         = {v : None for v in graph['vertices']}
    order          = {v : 0 for v in graph['vertices']}
    level          = {v : 0 for v in graph['vertices']}

    parent[root]   = root
    level[root]    = 0
    tree_height    = level[root]
    aux_order      = 1
    
    while(len(queue) > 0):
        vertice = queue.popleft()

        order[vertice] = aux_order
        aux_order      = aux_order + 1

        for neighboor in adjacency_list[vertice]:
            if parent[neighboor] == None:
                queue.append(neighboor)

                parent[neighboor] = vertice
                level[neighboor]  = level[vertice] + 1

                tree_height = max(tree_height, level[neighboor])

    return [parent, order], tree_height

def min_height_spanning_tree():
    graph = get_graph()

    min_height    = math.inf
    spanning_tree = None

    # Busca em largura com raiz em cada vértice do grafo
    for root in graph['vertices']:
        tree, tree_height = BFS(graph, root)

        if min_height > tree_height:
            min_height    = tree_height
            spanning_tree = tree

    return format_tree(spanning_tree)