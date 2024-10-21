import numpy as np

def solution(board):
    test = np.array(board)
    l = len(board)
    
    for i in range(l):
        for j in range(l):
            if board[i][j] == 1:
                min_x, min_y = max(0, i - 1), max(0, j - 1)
                man_x, max_y = min(l, i + 2), min(l, j + 2)

                test[min_x:man_x, min_y:max_y] = 2
                
    count = int(np.sum(test ==0))

    return count