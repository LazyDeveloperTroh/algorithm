# M번 더해서 최대의 수를 구함. 단 각 수는 K번 넘게 더할 수 없음
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

result = arr[0]*(M//K)*K + arr[1]*(M%K)
print(result)