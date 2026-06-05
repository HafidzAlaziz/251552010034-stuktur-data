class Graph:
    def __init__(self):
        self.graph = {
            "Lutpi": ["Abang", "Fajrul"],
            "Abang": ["Lutpi"],
            "Fajrul": ["Lutpi"]
        }
    
    def hapus_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
        if v in self.graph and u in self.graph[v]:
            self.graph[v].remove(u)
    
    def tampilkan_graph(self):
        print(self.graph)

g = Graph()
g.hapus_edge("Lutpi", "Fajrul")
g.hapus_edge("Lutpi", "Abang")
g.tampilkan_graph()