class Graph:
    def __init__(self):
        self.graph = {
            "Lutpi": ["Abang"],
            "Abang": ["Lutpi", "Fajrul"],
            "Fajrul": ["Abang"]
        }
    
    def search(self, start, target):
        visited = set()
        def dfs(v):
            if v == target:
                return True
            visited.add(v)
            for neighbor in self.graph.get(v, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False
        return dfs(start)
    
if __name__ == "__main__":
    g = Graph()
    print("Lutpi ke Fajrul ?", g.search("Lutpi", "Fajrul"))
    print("Lutpi ke Nabhan?", g.search("Lutpi", "Nabhan"))