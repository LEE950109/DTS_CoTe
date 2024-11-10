def solution(n, times):
    start, end = 0, max(times) * n 

    while start <= end:
        middle_time = (start + end) // 2  # 중간 시간 설정
        total_people = sum(middle_time // time for time in times)  # mid 시간 동안 처리할 수 있는 사람 수

        if total_people >= n:  # 모든 사람을 심사할 수 있는 경우
            answer = middle_time  # 현재 시간을 저장하고, 시간을 줄여 더 최적의 값을 찾음
            end = middle_time - 1
        else:  # 심사 인원이 부족한 경우, 시간을 늘림
            start = middle_time + 1

    return answer  # 최소 시간이 저장된 answer 반환



"""
import heapq

def solution(n, times):
    heap = [(time, time) for time in times]
    heapq.heapify(heap)

    out = 0

    while out < n:
        total_time, time = heapq.heappop(heap)  # 가장 작은 항목을 반환
        out += 1  # 나간 수

        if out == n:
            return total_time

        heapq.heappush(heap, (total_time + time, time))
"""
