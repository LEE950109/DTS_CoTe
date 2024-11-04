def solution(msg):
    answer = []
    max_len = 1
    num = 27
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lzw = {a.upper(): n+1 for n, a in enumerate(alphabet)}
    
    

    while msg:
        # if not msg:
        #     break
            
        if max_len > len(msg):
            max_len = len(msg)

        for n in range(max_len, 0, -1):
            if msg[:n] in lzw:
                answer.append(lzw[msg[0: n]])
                lzw[msg[0: n + 1]] = num

                max_len = max(max_len, n + 1)
                num += 1
                msg = msg[n:]
                break
    return answer

