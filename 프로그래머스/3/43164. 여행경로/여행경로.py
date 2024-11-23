from collections import deque

def solution(tickets):
    graph = {}
    for a, b in tickets:
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
    
    for key in graph:
        graph[key].sort()
    
    path = []
    tree = deque(["ICN"])
    
    while tree:
        current = tree[-1]
        if current in graph and graph[current]:
            next_destination = graph[current].pop(0)
            tree.append(next_destination)
        else:
            path.append(tree.pop())
    
    return path[::-1]

