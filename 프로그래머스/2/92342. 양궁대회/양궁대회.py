def cal_scores(ryan_score, apeach_score):
    ryan_total, apeach_total = 0, 0

    for i in range(11):
        if ryan_score[i] > apeach_score[i]:
            ryan_total += 10 - i
        elif apeach_score[i] > 0:
            apeach_total += 10 - i
    return ryan_total, apeach_total


def update_best_strategy(ryan_score, apeach_score, arrows_left, best, max_diff):
    # 남은 화살은 0점에 버리기 > for 문 돌릴 때 인텍스 에러 방지
    if arrows_left > 0:
        ryan_score[10] += arrows_left

    # 점수 계산
    ryan_total, apeach_total = cal_scores(ryan_score, apeach_score)
    diff = ryan_total - apeach_total

    # 전략 갱신 조건
    if diff > max_diff:
        max_diff = diff
        best = ryan_score[:]
    elif diff == max_diff and diff > 0:
        # 낮은 점수를 많이 맞힌 전략 선택
        for i in range(10, -1, -1):
            if ryan_score[i] > best[i]:
                best = ryan_score[:]
                break
            elif ryan_score[i] < best[i]:
                break

    # 0점에 버렸던 화살 다시 복구
    if arrows_left > 0:
        ryan_score[10] -= arrows_left
    return best, max_diff


def solution(n, info):
    max_diff = 0
    best_strategy = [-1] # 전략이 업데이트 안되는 경우 -1 리턴

    # (index, arrows_left, ryan_score)
    stack = [(0, n, [0] * 11)]

    while stack:
        index, arrows_left, ryan_score = stack.pop()

        # 탐색 종료 조건
        if index == 11 or arrows_left == 0:
            best_strategy, max_diff = update_best_strategy(
                ryan_score, info, arrows_left, best_strategy, max_diff
            )
            continue

        # 점수를 얻는 경우 남은 화살이 어피치의 특정 점수 화살 보다 높은 경우 추가
        if arrows_left > info[index]:
            new_score = ryan_score[:]
            new_score[index] = info[index] + 1
            stack.append((index + 1, arrows_left - new_score[index], new_score))

        # 점수를 포기 하는 경우 인텍스만 추가 해서 리턴 
        stack.append((index + 1, arrows_left, ryan_score[:]))

    return best_strategy