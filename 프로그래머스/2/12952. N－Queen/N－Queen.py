def check(n, q_y, position, dialog_ru, dialog_rd, ans):
    """
    queen이 위치 정의 y는 고려 안하고 x 위치만 생각 [1, 2 , 3, ```, n]
    dialog_ru: 왼쪽 아래에서 오른쪽 위로 올라가는 대각선 정의
      - (i, j) 일 때 i + j = const. 로 정의 >> n = 4이면 [0, 1, 2, 3, 4, 5, 6]
    dialog_rd: 왼쪽 위에서 오른쪽 아래로 내려가는 대각선 정의
      - (i, j) 일 때 i - j + n = const. 로 정의 >> n = 4 이면 [1, 2, 3, 4, 5, 6, 7]
    position: 퀸이 존재하는 열을 체크
    ans: list로 서언한 이유는 가변 객체로 정의해서 list를 도는 동안 값을 유지하기 위해서
      - 이 부분에서 ans를 재귀적으로 호출하면 왜 값이 유지되는지 정확하게 이해 못해서 그냥 전역으로 사용
    """
    if q_y == n: #
        ans[0] += 1
    else:
        for i in range(n):
            if position[i] == 0 and dialog_ru[i + q_y] == 0 and dialog_rd[i - q_y + n] == 0:
                position[i] = 1
                dialog_ru[i + q_y] = 1
                dialog_rd[i - q_y + n] = 1

                # 다음 행으로 재귀 호출
                check(n, q_y + 1, position, dialog_ru, dialog_rd, ans)

                # 백트래킹
                position[i] = 0
                dialog_ru[i + q_y] = 0
                dialog_rd[i - q_y + n] = 0

    return ans[0]

def solution(n):
    position = [0] * n
    dialog_ru = [0] * 2 * n
    dialog_rd = [0] * 2 * n
    ans = [0]  # 정답을 저장해 줄 값
    return check(n, 0, position, dialog_ru, dialog_rd, ans)