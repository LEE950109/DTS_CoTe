def backtrack(k, dungeons, visited, cnt):
    max_num = cnt
    
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and visited[i] == 0:
            visited[i] = 1
            max_num = max(max_num, backtrack(k-dungeons[i][1], dungeons, visited, cnt + 1))
            
            visited[i] = 0
            
    return max_num

            
def solution(k, dungeons):
    visited = [0]*len(dungeons)

    max_num = backtrack(k, dungeons, visited, 0)
    
    
    return max_num