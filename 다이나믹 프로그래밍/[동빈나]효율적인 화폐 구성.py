import sys
import math

n, m = map(int, input().split())
dp = [math.inf]*(m+1)

price = []
for _ in range(n):
    price.append(int(input()))

for p in price:
    if p < len(dp):
        dp[p] = 1
    
for i in range(1, m+1):
    for p in price:
        if i - p > 0 and dp[i-p] != math.inf:
            dp[i] = min(dp[i], dp[i-p])+1

    sumPrice = sum(price)
    if i % sumPrice == 0:
        dp[i] = min(dp[i], (i//sumPrice) * len(price))

for i in range(len(dp)):
    print(i, dp[i])