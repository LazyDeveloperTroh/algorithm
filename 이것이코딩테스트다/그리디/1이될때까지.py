N, K = map(int,input().split())

result = 0
while N != 1:
    if N%K == 0:
        N=N//K
    else:
        N-=1
    result += 1

print(result)