# https://www.acmicpc.net/problem/13305
# 1. 더 싼 기름이 나올 때까지 현재 기름을 기준으로 거리를 이동한다.
# 2. 마지막 마을의 기름값은 의미가 없다.
# 3. 이러한 문제 유형은 중요한 값(리터 당 가격)을 필요할 때(더 작은 가격이 있을 때) 변경하는 게 포인트인 것 같다.

n = int(input())
link = list(map(int, input().split()))
price = list(map(int, input().split()))

current_price = price[0]
total_price = current_price * link[0]
for i in range(1, len(link)):
    if current_price > price[i]:
        current_price = price[i]
    total_price += (current_price * link[i])

print(total_price)