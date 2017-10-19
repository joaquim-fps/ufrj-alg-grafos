graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F'],
    'edges': set([
        (9, 'A', 'B'),
        (4, 'B', 'C'),
        (7, 'C', 'D'),
        (2, 'D', 'E'),
        (1, 'A', 'F'),
        (20, 'B', 'D'),
        (10, 'C','F'),
        (3, 'D', 'F'),
        (7, 'C','E'),
        (9, 'B', 'A'),
        (4, 'C', 'B'),
        (7, 'D', 'C'),
        (2, 'E', 'D'),
        (1, 'F', 'A'),
        (20, 'D', 'B'),
        (10, 'F','C'),
        (3, 'F', 'D'),
        (7, 'E','C'),
    ])
}

def kruskal(graph):
    parent = dict()
    rank = dict()

    def make_set(vertice):
        parent[vertice] = vertice
        rank[vertice] = 1

    def find(vertice):
        if parent[vertice] != vertice:
            parent[vertice] = find(parent[vertice])
        return parent[vertice]

    def union(vertice1, vertice2):
        root1 = find(vertice1)
        root2 = find(vertice2)
        
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root1] = root2
                
                if rank[root1] == rank[root2]:
                    rank[root2] += 1
            
            return True
        else:
            return False

    for vertice in graph['vertices']:
        make_set(vertice)
        
    minimum_spanning_tree = set()
    
    edges = list(graph['edges'])
    edges.sort()

    for edge in edges:
        if union(edge[1], edge[2]):
            minimum_spanning_tree.add(edge)

            if len(minimum_spanning_tree) == len(graph['vertices'])-1:
                return minimum_spanning_tree

print(kruskal(graph))
