import heapq
from collections import defaultdict

def dfs(graph, stack, path):
    while stack:
        current = stack[-1]
        # 현재 공항에서 더 방문할 목적지가 있는 경우
        if graph[current]:
            # 힙에서 가장 사전순으로 빠른 목적지를 가져옴
            next_destination = heapq.heappop(graph[current])
            stack.append(next_destination)  # 다음 목적지 추가
        else:
            # 더 이상 갈 곳이 없으면 경로에 추가
            path.append(stack.pop())

def solution(tickets):
    # defaultdict를 사용하여 그래프를 생성
    graph = defaultdict(list)

    # 각 티켓 정보를 그래프에 추가
    for a, b in tickets:
        heapq.heappush(graph[a], b)  # 사전순으로 관리하기 위해 힙에 삽입

    # 최종 경로를 저장할 리스트
    path = []
    # 탐색 시작 공항은 "ICN"
    stack = ["ICN"]

    # DFS 수행
    dfs(graph, stack, path)
    
    # 역순으로 저장된 경로를 뒤집어서 반환
    return path[::-1]

