def solution(keyinput, board):
    max_w = board[0] // 2
    max_l = board[1] // 2
    ori = [0, 0]
    
    moves = {"up": [0, 1, max_w], "down": [0, -1,], "right": [1, 0], "left": [-1 ,0]}
    
    for key in keyinput:
        ori[0] += moves[key][0]
        ori[1] += moves[key][1]
        
        if ori[0] > max_w:
            ori[0] = max_w
        if ori[0] < -max_w:
            ori[0] = -max_w
        
        if ori[1] > max_l:
            ori[1] = max_l
        if ori[1] < -max_l:
            ori[1] = -max_l
        
    return ori