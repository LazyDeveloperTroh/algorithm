# from queue import PriorityQueue # thread safe
import heapq # none thread safe

def solution(scoville, K):
    q = []
    for scov in scoville:
        heapq.heappush(q, scov)

    answer = 0
    while q:
        min1 = heapq.heappop(q)
        # 최소 스코빌이 K이상이라 LOOP 탈출
        if min1 >= K:
            break
        
        # 큐에 더이상 혼합할 스코빌이 없을때, K이상의 스코빌을 만들 수 없다..
        if not q:
            answer = -1
            break
        min2 = heapq.heappop(q)

        # 스코빌 혼합 후 큐에 저장, 횟수 1증가
        mix = min1 + 2*min2
        heapq.heappush(q, mix)
        answer += 1
    return answer

print(solution([1, 2, 3, 9, 10, 12]	, 7))