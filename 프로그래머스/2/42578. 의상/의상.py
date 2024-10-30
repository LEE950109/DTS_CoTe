def solution(clothes):
    dict_clothes = {}
    for value, key in clothes:
        if key in dict_clothes:
            dict_clothes[key] += 1
        else:
            dict_clothes[key] = 1
    print(dict_clothes)
    
    num = 1
    for k in dict_clothes:
        num *= (dict_clothes[k]+1)
    
    return num -1