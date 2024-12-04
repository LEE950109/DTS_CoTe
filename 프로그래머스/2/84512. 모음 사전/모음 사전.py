
def solution(word):
    """    
    탐색을 하려면 전체를 다 계산해서 비효율적일거 같아서 미리 각 자리의 경우를 계산
    1번 자리 = 5^4 + 5^3 + 5^2 + 5 + 1
    2번 자리 = 5^3 + 5^2 + 5 + 1
    
    이런식으로 계산 > cases_cnt = [781, 156, 31, 6, 1]
    """
    
    words = ['A', 'E', 'I', 'O', 'U']
    cases_cnt = [sum(5**i for i in range(j)) for j in range(5, 0, -1)] # 각 자리에서의 경우의 수
    
    result = 0
    for i, w in enumerate(word):
        # 각 문자의 위치에서 경우의 수와 현재 위치 +1 을 해서 경우를 계산
        index = words.index(w)
        result += index * cases_cnt[i] + 1
    
    return result

# 이 부분은 백트래킹으로 구한 부분 > 근데 백트래킹인지 잘 모르겠음 
"""
def solution(word):
    words = ['A', 'E', 'I', 'O', 'U']
    result = []
    target = word
    found = False
    
    def dfs(current_word):
        
        # 정답 발견 시, 조기 종료를 위한 부분 없으면 전체 탐색까지 탐색 계속됨
        found nonlocal 
        if found:
            return 
        result.append(current_word)
        # 정답이면 종료
        if current_word == target:
            found = True
            return 
        # 단어의 길이 5개면 반환
        if len(current_word) >= 5:
            return 
        # 재귀 함수로 단어 탐색
        for w in words:
            dfs(current_word + w)
    # 탐색 시작
    for w in words:
        dfs(w)

    # 찾은 단어의 인덱스 반환
    return result.index(word) + 1
"""