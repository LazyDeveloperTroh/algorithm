import sys
input = sys.stdin.readline

n = int(input())
arrays = []
for _ in range(n):
    arrays.append(int(input()))

if n == 1:
    print(arrays[0])
elif n == 2:
    print(arrays[0]+arrays[1])
elif n == 3:
    print(max(arrays[0]+arrays[2], arrays[1]+arrays[2]))
else:
    dp = [0] * n
    dp[0] = arrays[0]
    dp[1] = arrays[0]+arrays[1]
    dp[2] = max(arrays[0]+arrays[2], arrays[1]+arrays[2])

    # i번째 계단을 밟는 경우는 2가지
    # i-3 계단을 밟고 i-1 계단과, i계단을 밟는 경우
    # i-2 계단을 밟고 i계단을 밟는 경우
    for i in range(3, n):
        dp[i] = max(dp[i-3]+arrays[i-1]+arrays[i], dp[i-2]+arrays[i])
    print(dp[n-1])