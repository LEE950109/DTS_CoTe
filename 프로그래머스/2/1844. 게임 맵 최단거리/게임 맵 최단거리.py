from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    directions = [[-1,0], [1,0], [0,-1], [0,1]]

    visited = [[-1] * m for _ in range(n)]
    visited[0][0] = 1

    dist_map = deque([[0,0,1]])

    while dist_map:
        x, y, dist = dist_map.popleft()

        if x == n - 1 and  y == m - 1:
            return dist

        for d in directions:
            x_ = x + d[0]
            y_ = y + d[1]

            if x_ < 0 or x_ >= n or y_ < 0 or y_ >= m:
                continue

            if maps[x_][y_] == 0:
                continue

            if visited[x_][y_] == 1:
                continue

            visited[x_][y_] = 1
            dist_map.append([x_, y_, dist + 1])

    return -1

