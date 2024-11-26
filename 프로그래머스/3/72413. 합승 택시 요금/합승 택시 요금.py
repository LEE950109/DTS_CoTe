import heapq  # 우선순위 큐를 위한 힙큐 모듈

# 다익스트라 알고리즘을 사용하여 최단 거리를 계산하는 함수
def dijkstra(start, n, graph):
    inf = float('inf')  # 무한대를 표현하기 위한 값
    distances = [inf] * (n + 1)  # 시작 노드로부터 각 노드까지의 거리를 저장할 리스트 (초기값은 무한대)
    distances[start] = 0  # 시작 노드의 거리는 0으로 설정
    queue = [(0, start)]  # (거리, 노드) 형태로 우선순위 큐에 추가
    
    while queue:  # 큐가 빌 때까지 반복
        current_dist, current_node = heapq.heappop(queue)  # 현재 가장 짧은 거리를 가진 노드 꺼내기
        if current_dist > distances[current_node]:  # 이미 더 짧은 경로가 있다면 무시
            continue
        for neighbor, weight in graph[current_node]:  # 현재 노드의 모든 이웃 노드 탐색
            distance = current_dist + weight  # 현재 노드까지의 거리 + 이웃 노드로 가는 거리
            if distance < distances[neighbor]:  # 새로 계산한 거리가 기존 거리보다 짧으면 갱신
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))  # 큐에 새로운 거리와 노드 추가
    return distances  # 시작 노드로부터 각 노드까지의 최단 거리 반환


# 문제 해결 함수
def solution(n, s, a, b, fares):
    # 그래프 생성
    graph = [[] for _ in range(n + 1)]  # 각 노드에 연결된 (이웃 노드, 거리) 저장
    for c, d, f in fares:
        graph[c].append((d, f))  # 노드 c에서 d로 가는 비용 f 추가
        graph[d].append((c, f))  # 노드 d에서 c로 가는 비용 f 추가 (양방향)

    # 각 노드로부터 다른 노드까지의 최단 거리 계산
    dist_from_s = dijkstra(s, n, graph)  # 시작점 s에서 각 노드까지의 최단 거리
    dist_from_a = dijkstra(a, n, graph)  # a에서 각 노드까지의 최단 거리
    dist_from_b = dijkstra(b, n, graph)  # b에서 각 노드까지의 최단 거리

    # 최소 비용 계산
    answer = float('inf')  # 최소 비용을 무한대로 초기화
    for t in range(1, n + 1):  # 모든 노드 t를 중간 지점으로 고려
        # s -> t + t -> a + t -> b 의 비용 계산
        answer = min(answer, dist_from_s[t] + dist_from_a[t] + dist_from_b[t])
    
    return answer  # 최소 비용 반환
