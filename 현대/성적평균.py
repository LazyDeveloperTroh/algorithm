import sys
from collections import deque

N, K = map(int, input().split())
S = list(map(int, input().split()))

ranges = []
for _ in range(K):
    start, end = map(int, input().split())
    sum = 0
    for i in range(start-1, end):
        sum += S[i]

    print("%.2f" % (round(sum/(end-start+1), 2)))
