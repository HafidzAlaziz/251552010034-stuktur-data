class Graph:
    def __init__(self):
        self.graph = {
            "Lutpi": ["Abang", "Fajrul"],
            "Abang": ["Lutpi", "Nabhan"],
            "Fajrul": ["Lutpi", "Yahya"],
            "Nabhan": ["Abang"],
            "Yahya": ["Fajrul"]
        }
    
    def bfs(self, start):
        visited = set()
        queue = [start]
        result = []

        while queue:
            v = queue.pop(0)
            if v not in visited:
                visited.add(v)
                result.append(v)
                queue.extend([n for n in self.graph[v] if n not in visited])
        return result

g = Graph()
print("Traversal BFS dari Lutpi:", g.bfs("Lutpi"))