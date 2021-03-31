# [해결전략]
# 큰 단위의 동전부터 최대한 거슬러준다.
# 복잡도는 동전종류수와 같음 N(K) ?
n = 1000-int(input())
coin_list = [500, 100, 50, 10, 5, 1]

cnt = 0
for coin in coin_list:
    cnt += int(n//coin)
    n%=coin
print(cnt)