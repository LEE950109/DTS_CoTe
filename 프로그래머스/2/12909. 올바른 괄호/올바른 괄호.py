def solution(s):
    stack = []
    
    for pt in s:       
        if pt == '(':
            stack.append(pt)
        elif pt == ')':
            if not stack:
                return False
            else:
                stack.pop()        
    
    if stack:
        return False
    else:
        return True
