class Graph:
    def __init__(self):
        self.graph = {
            "Lutpi": ["Abang", "Fajrul"],
            "Abang": ["Lutpi"],
            "Fajrul" : ["Lutpi"]
        }
    
    def hapus_vertex(self, vertex):
        if vertex in self.graph:
            self.graph.pop(vertex)
            for v in self.graph:
                if vertex in self.graph[v]:
                    self.graph[v].remove(vertex)

    def tampilkan_graph(self):
        print(self.graph)

g = Graph()
g.hapus_vertex("Lutpi")
g.tampilkan_graph()