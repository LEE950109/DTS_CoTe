def dfs(graph, tree, path):
    while tree:
        current = tree[-1]
        if current in graph and graph[current]:
            next_destination = graph[current].pop(0)
            tree.append(next_destination)
        else:
            path.append(tree.pop())

def solution(tickets):
    graph = {}
    for a, b in tickets:
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
    
    for key in graph:
        graph[key].sort()
    
    path = []
    tree = ["ICN"]  # 리스트를 사용하는 간단한 스택으로 변경
    
    dfs(graph, tree, path)
    
    return path[::-1]

