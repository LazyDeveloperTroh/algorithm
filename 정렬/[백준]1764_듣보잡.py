# n 듣도못한 m 보도못한
n, m = map(int, input().split())

# 듣도못한 사람은 dict, 보고못한 사람은 list에 저장
dict1 = {}
for _ in range(n):
    s = input()
    dict1[s] = 1

arr2 = []
for _ in range(m):
    arr2.append(input())

# 보도못한 사람이 듣도못한 사람과 중복되는지 확인
result = []
for s2 in arr2:
    if s2 in dict1:
        result.append(s2)

result.sort()
print(len(result))
for r in result:
    print(r, end=" ")