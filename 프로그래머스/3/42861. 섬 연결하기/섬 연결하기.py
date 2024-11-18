def solution(n, costs):
    # 비용 기준으로 간선 정렬
    costs.sort(key=lambda x: x[2])
    
    # 각 섬을 독립된 집합으로 초기화
    sets = [set([i]) for i in range(n)]
    total_cost = 0
    
    for a, b, cost in costs:
        # 두 섬이 이미 같은 집합에 속해 있다면 무시
        set_a = next(s for s in sets if a in s)
        set_b = next(s for s in sets if b in s)
        if set_a != set_b:
            # 두 집합을 병합
            set_a.update(set_b)
            sets.remove(set_b)
            total_cost += cost
        
        # 모든 섬이 하나의 집합으로 통합되었으면 종료
        if len(sets) == 1:
            break
    
    return total_cost