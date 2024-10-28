def solution(priorities, location):
    max_q = max(priorities)
    l = len(priorities)
    target_num = priorities[location]
    target = l-location

    order = 1

    while True:
        print(target, l, order)
        print(max_q, priorities)

        if priorities[0] != max_q:
            priorities.append(priorities.pop(0))
            target = (target + 1)%l
        else:
            if max_q == target_num and target % l == 0:
                break

            priorities.pop(0)
            max_q = max(priorities)
            order += 1

            l -= 1
    print(order)
    return order
