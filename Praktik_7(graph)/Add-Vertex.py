class Graph:
    def __init__(self):
        self.graph = {}
    
    def tambah_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def tampilkan_graph(self):
        print(self.graph)

g = Graph()
g.tambah_vertex("Lutpi")
g.tambah_vertex("Abang")
g.tampilkan_graph()