def solution(bridge_length, weight, truck_weights):
    t = 0
    on_bridge = {}
    
    while truck_weights:
        t += 1
        on_bridge.pop(t - bridge_length, None)
        
        if len(on_bridge) <= bridge_length and sum(on_bridge.values()) + truck_weights[0] <= weight:
            on_bridge[t] = truck_weights.pop(0)

        
    return t + bridge_length