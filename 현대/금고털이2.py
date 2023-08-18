import sys
input = sys.stdin.readline

w, n = map(int, input().split())

datas = []
for _ in range(n):
    m, p = map(int, input().split())
    datas.append([m, p])

# price 오름차순 정렬
datas.sort(key=lambda x:x[1], reverse=True)
print(datas)

result = 0
for i in range(len(datas)):
    m, p = datas[i][0], datas[i][1]
    if w >= m:
        w -= m
        result += m*p
    else:
        result += w*p
        w = 0
print(result)

