def solution(info, edges):
    tree = [[] for _ in range(len(info))]
    for edge in edges:
        tree[edge[0]].append(edge[1])
        
    status = [[0, 1, 0, set()]]
    max_sheep = 0

    while status:
        now, sheep, wolf, nodes = status.pop(0)
        max_sheep = max(max_sheep, sheep)
        nodes.update(tree[now])

        print(nodes)

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
