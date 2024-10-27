from collections import deque


def solution(bridge_length, weight, truck_weights):
    t = 0
    times = deque() # 트럭이 다리 위에 들어가는 시간
    on_bridge = deque() # 다리 위 트럭
    truck_weights = deque(truck_weights)
    
    # 트럭의 다리 진입 시간과 다리 위 트럭을 기록해서 비교 
    while truck_weights:
        t += 1
        
        # 트럭이 다리 위에 진입 하고 Length만큼 시간이 지나면 times와 bridge에서 제거 
        if times and times[0] == t - bridge_length: 
            times.popleft()
            on_bridge.popleft()
        
        exp_weights = sum(on_bridge) + truck_weights[0] # 예상 다리 위 트럭의 무게 합
        
        # 트럭이 길이 보다 적고 무게가 초과하지 않았으면 다리 위에 트럭과 해당 시간 추가 
        if len(on_bridge) <= bridge_length and exp_weights <= weight:
            on_bridge.append(truck_weights.popleft())
            times.append(t)

    # 마지막 기록 시간과 해당 트럭이 빠져나가는데 걸린 시간을 합산하여 반환
    return t + bridge_length