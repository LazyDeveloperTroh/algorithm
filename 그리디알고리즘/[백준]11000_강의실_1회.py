import sys
import heapq

input = sys.stdin.readline
n = int(input())

arr = []
for _ in range(n):
    start, end = map(int, input().split())
    arr.append([start, end])

# 수업 시작시간을 기준으로 정렬
arr.sort(key= lambda x : x[0])

que = []
heapq.heappush(que, arr[0][1])
for i in range(1, n):
    start, end = arr[i][0], arr[i][1]
    # 수업이 가장 빨리 끝나는 시간과 수업 시작 시간을 비교
    # 왜 첫 번째랑만 비교하느냐? 첫번째가 중복되면 그 이후는 무조건 중복되기 때문에..
    if start < que[0]:
        heapq.heappush(que, end)
    else:
        heapq.heappop(que)
        heapq.heappush(que, end)

print(len(que))
