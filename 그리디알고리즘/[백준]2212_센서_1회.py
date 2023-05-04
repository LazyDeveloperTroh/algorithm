import sys

n = int(input())
k = int(input())
arr = list(map(int, input().split()))

arr.sort()

# 센서간의 거리를 오름차순으로 정리한다.
dist = []
for i in range(1, n):
    dist.append(arr[i]-arr[i-1])
dist.sort()

# n개의 센서 중 k개의 수신탑을 세웠기 때문에 n-k개의 센서거리 최솟값을 구하면 된다.
result = 0
for i in range(n-k):
    result += dist[i]

print(result)