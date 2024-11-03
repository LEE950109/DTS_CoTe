def solution(msg):
    answer = []
    lzw = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
           'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
           'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
           'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, }

    max_len = 1
    num = 27

    while True:

        if not msg:
            break

        if max_len > len(msg):
            max_len = len(msg)

        for n in range(max_len, 0, -1):
            if msg[:n] in lzw:
                answer.append(lzw[msg[0: n]])
                lzw[msg[0: n + 1]] = num

                if max_len < n+1:
                    max_len = n + 1
                    
                num += 1
                msg = msg[n:]

                break

    return answer

