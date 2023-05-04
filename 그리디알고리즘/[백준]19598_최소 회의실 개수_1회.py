import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    start, end = map(int, input().split())
    arr.append([start, end])

arr.sort()

que = []
heapq.heappush(que, arr[0][1])
for i in range(1, n):
    start, end = arr[i][0], arr[i][1]

    if start < que[0]:
        heapq.heappush(que, end)
    else:
        heapq.heappop(que)
        heapq.heappush(que, end)

print(len(que))