from sys import stdin;
from copy import deepcopy;

N, K = map(int, stdin.readline().split())

arr = list(map(int, stdin.readline().split()))
for i in range(1, N-1):
    print(arr[i])