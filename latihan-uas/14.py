from collections import deque

graf = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(graf, start):
    visited = []
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graf[node])
    return visited

hasil_bfs = bfs(graf, 'A')
print(f"BFS dari A: {hasil_bfs}")