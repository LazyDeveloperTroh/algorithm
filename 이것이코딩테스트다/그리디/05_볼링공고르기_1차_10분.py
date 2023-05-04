# n의 범위가 1000이라서 큰 문제가 없을 수 있지만 범위가 커진다면 타임아웃의 가능성이 높다.
# 해설집의 풀이와 차이가 크다..
n, k = map(int, input().split())
input_datas = list(map(int, input().split()))

result = 0
for i in range(n-1):
    for j in range(i+1, n):
        if input_datas[i] != input_datas[j]:
            result += 1
print(result)