def solution(n, words):
    answer = [0, 0]
    check_len = set()
    l_before = 0
    end = words[0][0]
    
    for i, word in enumerate(words):
        check_len.add(word)
        l_now = len(check_len)

        if l_now == l_before or end != word[0]:
            return [i%n + 1, i//n + 1]
        else:
            l_before = l_now
            end = word[-1]

    return answer