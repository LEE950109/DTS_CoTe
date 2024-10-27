# goal의 전체 길이가 20이하로 제한 되므로 그냥 queue 사용

def solution(cards1, cards2, goal):
    
    # goal 전체를 탐색하고 cards1과 cards2 중에 같은 곳이 있으면 pop
    while goal:
        if len(cards1) > 0 and cards1[0] == goal[0]:
            cards1.pop(0)
            goal.pop(0)
            
        elif len(cards2) > 0 and cards2[0] == goal[0]:
            cards2.pop(0)
            goal.pop(0)
            
        else:
            break

    # 만약 goal이 존재 하지않으면 "Yes", goal이 남아 있으면 "No" 
    if not goal:
        return "Yes"
    else:
        return "No"