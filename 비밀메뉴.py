import sys
input = sys.stdin.readline

M, N, K = map(int, input().split())
secret = list(map(int, input().split()))
datas = list(map(int, input().split()))

matched = False
for i in range(N-M+1):
    if secret[0] == datas[i]:
        matched = True
        for j in range(M):
            if datas[i+j] != secret[j]:
                matched = False
                break
        if matched:
            break

if matched:
    print("secret")
else:
    print("normal")