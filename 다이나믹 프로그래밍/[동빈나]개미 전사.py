n = int(input())
array = list(map(int, input().split()))
dp = [0] * n
dp[0]=array[0]
dp[1]=max(dp[0], array[1])
for i in range(2, len(array)):
    dp[i] = max(array[i]+dp[i-2], dp[i-1])

print(dp)