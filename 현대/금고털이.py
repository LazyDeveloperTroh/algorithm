import sys
input = sys.stdin.readline

W, N = map(int, input().split())

datas = []
for _ in range(N):
    m, p = map(int, input().split())
    datas.append((m,p))

# 가격 내림차순 정렬
datas = sorted(datas, key=lambda x:-x[1])

maxPrice = 0
for m, p in datas:
    if W >= m:
        maxPrice += m*p
        W -= m
    else:
        maxPrice += W*p
        W = 0
print(maxPrice)