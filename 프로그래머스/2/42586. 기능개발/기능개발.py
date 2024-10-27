from collections import deque
from math import ceil

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    

    max_n = ceil((100 - progresses[0]) / speeds[0])
    s = 0
    service = []
    
    
    while progresses:
        num = ceil(100 - progresses.popleft()) / speeds.popleft()

        if max_n >= num:
            s += 1
        else:
            max_n = num
            service.append(s)
            s = 1            

    service.append(s)   
    return service