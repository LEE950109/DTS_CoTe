from collections import deque

def solution(info, edges):
    tree = [[] for _ in range(len(info))]
    for edge in edges:
        tree[edge[0]].append(edge[1])
        
    status = [[0, 1, 0, set()]]
    status = deque(status)
    max_sheep = 0

    while status:
        now, sheep, wolf, nodes = status.popleft()
        max_sheep = max(max_sheep, sheep)
        nodes.update(tree[now])

        for node in nodes:
            if info[node] == 1:
                if sheep > wolf + 1:
                    status.append(
                        [node, sheep, wolf + 1, nodes - {node}]
                    )
            else:
                status.append(
                    [node, sheep + 1, wolf, nodes - {node}]
                )
    return max_sheep
