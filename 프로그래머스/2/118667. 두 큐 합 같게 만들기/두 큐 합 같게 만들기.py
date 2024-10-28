from collections import deque


def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    sum1 = sum(queue1)
    sum2 = sum(queue2)

    target = (sum1 + sum2) / 2

    # 두 큐 합이 정수로 나누어지지 않으면 불가능하므로 -1 반환
    if target != int(target):
        return -1

    target = int(target)
    t = 0
    max_op = (len(queue1) + len(queue2)) * 2  # 최대 연산 횟수 제한 > 가운데 값을 기준으로 주고 받는 경우의 수 

    # 투 포인터 방식을 사용해 각 큐를 관리
    while t < max_op:
        if sum1 == target:
            return t
        
        elif sum1 > target:
            q = queue1.popleft()
            sum1 -= q
            queue2.append(q)
            
        else:
            q = queue2.popleft()
            sum1 += q
            queue1.append(q)

        t += 1

    return -1