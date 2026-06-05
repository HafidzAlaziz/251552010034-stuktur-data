class Graph:
    def __init__(self):
        self.graph = {}
    
    def tambah_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def tampilkan_graph(self):
        print(self.graph)

g = Graph()
g.tambah_edge("Lutpi", "Abang")
g.tambah_edge("Lutpi", "Fajrul")
g.tampilkan_graph()