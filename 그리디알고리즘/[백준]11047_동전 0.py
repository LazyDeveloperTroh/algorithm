# [해결전략]
# 여러 동전을 사용해서 K원을 만들어야 하는데 동전의 개수를 최소로 해야한다는 것은
# 큰 금액의 동전부터 최대한 거슬러줘야 한다는 것. 여기서 전제조건은 A(i)는 A(i-i)의 배수라는 것
# 쉽게말하면 A(i-1) 동전을 2개 주는것보다 A(i)의 동전을 1개 주는게 문제를 해결하는데 도움이 된다는 것

N, K = map(int, input().split())

# 동전종류 
money_list = []
for i in range(N):
    money_list.append(int(input()))

# 단위가 큰 동전부터 나열
money_list.sort(reverse=True)

cnt = 0
for money in money_list:
    cnt += int(K//money)
    K = K%money

print(cnt)