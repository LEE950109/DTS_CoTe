from collections import deque


def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    target = (sum1 + sum2) / 2

    if target != int(target):
        return -1

    target = int(target)
    t = 0
    max_op = (len(queue1) + len(queue2)) * 2 

    while t < max_op:
        if sum1 == target:
            return t
        elif sum1 > target:
            value = queue1.popleft()
            sum1 -= value
            queue2.append(value)
        else:
            value = queue2.popleft()
            sum1 += value
            queue1.append(value)

        t += 1

    return -1