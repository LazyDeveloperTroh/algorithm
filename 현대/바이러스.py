import sys

input = sys.stdin.readline
K, P, N = map(int, input().split())
M = 1000000007

result = K*P
for _ in range(N-1):
    result = result%M * P%M 
print(result%M)