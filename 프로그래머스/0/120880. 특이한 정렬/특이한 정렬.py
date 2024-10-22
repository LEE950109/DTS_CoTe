def solution(numlist, n):
    test = {}
    distance = []
    epsilon = 0.00001
    for i in numlist:
        if i-n < 0:
            distance += [n - i]
        else:
            distance += [i - n - epsilon]

    sorted_distance = sorted(distance)
    result = [numlist[distance.index(dis)] for dis in sorted_distance]
    return result