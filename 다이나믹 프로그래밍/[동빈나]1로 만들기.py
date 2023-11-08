import math

n = int(input())
dp = [math.inf]*(n+1)
dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[5] = 1

for i in range(2, n+1):
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i//5])+1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3])+1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2])+1
    if dp[i-1] < dp[i]:
        dp[i] = dp[i-1]+1

print(dp[n])