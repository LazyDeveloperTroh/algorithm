N, M = map(int, input().split())

result = 1
for i in range(N):
    row = list(map(int, input().split()))
    if min(row) > result:
        result = min(row)

print(result)