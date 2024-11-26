from collections import deque  # BFS(너비 우선 탐색)에 사용할 데크(deque) 모듈을 가져옴

# 문제 해결 함수
def solution(numbers, target):
    # BFS를 위한 큐 초기화 (초기 상태: 인덱스 0, 현재 합계 0)
    tree = deque([(0, 0)])  
    count = 0  # 목표(target) 숫자를 만드는 경우의 수를 저장할 변수
    
    # BFS 탐색 시작
    while tree:
        index, current_sum = tree.popleft()  # 큐에서 현재 상태를 꺼냄
        
        # 모든 숫자를 탐색했을 때
        if index == len(numbers):
            if current_sum == target:  # 목표 값과 합계가 같으면
                count += 1  # 경우의 수를 증가
        else:
            # 현재 숫자를 더한 경우를 큐에 추가
            tree.append((index + 1, current_sum + numbers[index]))
            # 현재 숫자를 뺀 경우를 큐에 추가
            tree.append((index + 1, current_sum - numbers[index]))
    
    # 목표 값을 만들 수 있는 경우의 수 반환
    return count
