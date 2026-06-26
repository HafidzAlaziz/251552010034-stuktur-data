graf = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [],
    6: []
}

def dfs_recursive(graf, node, visited=None):
    if visited is None:
        visited = []
    if node not in visited:
        visited.append(node)
        for tetangga in graf[node]:
            dfs_recursive(graf, tetangga, visited)
    return visited

hasil_dfs = dfs_recursive(graf, 1)
print(f"DFS dari 1: {hasil_dfs}")