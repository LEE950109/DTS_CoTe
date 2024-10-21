def solution(my_string):
    num_list = my_string.split()
    num = int(num_list[0])

    for i in range(1, len(num_list), 2):
        if num_list[i] == '+':
            num += int(num_list[i+1])
        elif num_list[i] == '-':
            num -= int(num_list[i+1])
            
    return num