def solution(clothes):
    dict_clothes = {}
    num = 1 # 경우의 수를 담을 변수
    
    # {category: number of clothes} 의 형태
    for value, key in clothes:
        if key in dict_clothes:
            dict_clothes[key] += 1
        else:
            dict_clothes[key] = 1
    
    # (n+1)(m+1)... > +1: 각 카테고리를 포함하지 않는 경우 0을 포함해서 
    for k in dict_clothes:
        num *= (dict_clothes[k]+1)
    
    # 옷을 안입는 경우를 제외하고 반환
    return num -1