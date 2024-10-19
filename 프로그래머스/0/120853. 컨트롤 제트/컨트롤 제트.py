def solution(s):
    s_list = s.split()
    sum = 0
    
    for i in range(len(s_list)):
        if s_list[i] == 'Z':
            sum -= int(s_list[i-1])
        else:
            sum += int(s_list[i])

    return sum