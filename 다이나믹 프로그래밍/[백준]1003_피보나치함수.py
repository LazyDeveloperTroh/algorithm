t = int(input())

dp = [[0 for j in range(2)] for i in range(41)]

dp[0] = [1, 0]
dp[1] = [0, 1]
for _ in range(t):
    n = int(input())
    for i in range(2, n+1):
        dp[i] = [i1 + i2 for i1, i2 in zip(dp[i-1], dp[i-2])]
    print(dp[n][0], dp[n][1])