graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['E', 'C'])
}

def bfs(start):
    queue = [start]
    levels = {}  
    levels[start] = 0
    visited = set([start])
    
    while queue:
        node = queue.pop(0)
        neighbours = graph[node]
        
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
                levels[neighbour] = levels[node] + 1
    
    print(levels)
    return visited

print(str(bfs('A')))
