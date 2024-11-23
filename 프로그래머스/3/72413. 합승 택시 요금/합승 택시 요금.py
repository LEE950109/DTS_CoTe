import heapq

def dijkstra(start, n, graph):
    inf = float('inf')
    distances = [inf] * (n + 1)
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_dist, current_node = heapq.heappop(queue)
        if current_dist > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances


def solution(n, s, a, b, fares):
    # 그래프 생성
    graph = [[] for _ in range(n + 1)]
    for c, d, f in fares:
        graph[c].append((d, f))
        graph[d].append((c, f))
    
    # 최단 거리 계산
    dist_from_s = dijkstra(s, n, graph)
    dist_from_a = dijkstra(a, n, graph)
    dist_from_b = dijkstra(b, n, graph)
    
    # 최소 비용 계산
    answer = float('inf')
    for t in range(1, n + 1):
        answer = min(answer, dist_from_s[t] + dist_from_a[t] + dist_from_b[t])
    
    return answer