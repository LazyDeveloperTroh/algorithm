import heapq, sys
input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    arrays = list(map(int, input().split()))

    for a in arrays:
        if len(h) == n:
            if a > h[0]:
                heapq.heappop(h)
                heapq.heappush(h, a)    
        else:
            heapq.heappush(h, a)

print(h[0])