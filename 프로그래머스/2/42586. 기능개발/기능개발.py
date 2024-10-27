from collections import deque
from math import ceil


def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    max_n = ceil((100 - progresses[0]) / speeds[0]) # 첫번째 수의 개발 시간 계산
    s = 0
    service = []
    
    while progresses:
        num = ceil(100 - progresses.popleft()) / speeds.popleft() # 각 progress의 필요 시간
        
        # max가 크면 배포되는 서비스 수에 +1
        if max_n >= num: 
            s += 1
                   
        # max가 작으면 max를 현재 num, 서비스 수를 1로 초기화 
        else: 
            max_n = num
            service.append(s)
            s = 1            

    service.append(s)   # while문 종료 후 최종 s 추가
    return service