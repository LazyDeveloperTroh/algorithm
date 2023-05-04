n = int(input())
d = [0] * 1000001

for i in range(2, n+1):
    # 1을 더했을 때
    d[i] = d[i-1]+1
    # i가 3으로 나눠질 때
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    # i가 2로 나눠질 때
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
print(d[n])