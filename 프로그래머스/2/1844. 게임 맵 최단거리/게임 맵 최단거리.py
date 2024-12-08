from collections import deque

"""
전체 맵의 크기를 구한 후, 깊이 탑색으로 문제 해결 

direction: 갈 수 있는 곳을 리스트로 저장
visited: 방문 했던 곳을 list로 표현 (1: 방문, -1: 방문x)
dist_map: 현재 위치와 거리를 저장 [0, 0, 1]

갈 수 있는 곳을 한 칸씩 이동하므로 제일 처음 도착했을 때가 최단거리 
만약 모든 경로를 다갔지만 도착하지 못했다면 -1 반환
"""

def solution(maps):
    # 전체 맵의 크기
    n = len(maps)
    m = len(maps[0])

    directions = [[-1,0], [1,0], [0,-1], [0,1]]
    
    # 방문 했던 곳을 표시할 리스트
    visited = [[-1] * m for _ in range(n)]
    visited[0][0] = 1
    
    # 현재 방문한 위치의 정보와 거리를 데큐로 저장
    dist_map = deque([[0,0,1]])
    
    # while문으로 bfs 구현 
    while dist_map:
        x, y, dist = dist_map.popleft()
        
        # 방문한 위치가 최종 목적지면 거리 반환
        if x == n - 1 and  y == m - 1:
            return dist
        
        # 갈 수 있는 모든 방향 탐색
        for d in directions:
            x_ = x + d[0]
            y_ = y + d[1]
            
            # 갈 수 있는 곳이 아니면 continue
            if x_ < 0 or x_ >= n or y_ < 0 or y_ >= m:
                continue
            if maps[x_][y_] == 0:
                continue
            if visited[x_][y_] == 1:
                continue
            
            # 방문한 곳을 1로 변경하고 dist_map에 지금 위치 추가 
            visited[x_][y_] = 1
            dist_map.append([x_, y_, dist + 1])
    return -1

