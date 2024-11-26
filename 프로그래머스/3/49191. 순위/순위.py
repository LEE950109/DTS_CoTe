from collections import deque

# BFS(너비 우선 탐색) 함수 정의
def bfs(start, graph):
    visited = set()  # 방문한 노드를 기록할 집합
    queue = deque([start])  # 탐색을 시작할 노드를 큐에 추가
    
    while queue:  # 큐가 비어있을 때까지 반복
        current = queue.popleft()  # 큐에서 노드를 꺼냄
        
        # 현재 노드의 이웃 노드들을 탐색
        for neighbor in graph[current]:
            if neighbor not in visited:  # 이웃 노드가 방문되지 않았다면
                visited.add(neighbor)  # 방문 표시
                queue.append(neighbor)  # 큐에 추가
    return visited  # 탐색한 노드 집합 반환


# 문제 풀이 함수 정의
def solution(n, results):
    answer = 0  # 정확한 순위를 알 수 있는 선수 수를 저장할 변수
    win_graph = [set() for _ in range(n + 1)]  # 이긴 선수 정보를 저장할 그래프
    lose_graph = [set() for _ in range(n + 1)]  # 진 선수 정보를 저장할 그래프
    
    # 경기 결과를 통해 그래프 구축
    for winner, loser in results:
        win_graph[winner].add(loser)  # 이긴 선수가 진 선수를 기록
        lose_graph[loser].add(winner)  # 진 선수가 이긴 선수를 기록
        
    # 각 선수에 대해 탐색
    for i in range(1, n + 1):
        wins = bfs(i, win_graph)  # i 선수가 이길 수 있는 모든 선수 탐색
        losses = bfs(i, lose_graph)  # i 선수를 이긴 모든 선수 탐색
        
        # 이긴 선수와 진 선수의 합이 n-1이면 순위가 명확
        if len(wins) + len(losses) == n - 1:
            answer += 1  # 정확한 순위를 알 수 있는 선수 수 증가
    
    return answer  # 결과 반환



