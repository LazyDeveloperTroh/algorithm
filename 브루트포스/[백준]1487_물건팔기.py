# 최대이익을 내려면 최대한 비싼가격에 팔고, 배송비는 낮아야함.
# 각 사람당 이익나는 금액을 계산한다면?

def get_benefit(fix_price, prices, ships):
    benefit = 0
    for i in range(len(prices)):
        # 고객이 생각한 가격보다 비싸다면 팔지못함
        if prices[i] < fix_price:
            continue
        # 상품가격보다 배송비가 더 나간다면 안파는게 이득
        if fix_price < ships[i]:
            continue
        benefit += (fix_price-ships[i])
    return benefit


N = int(input())

# 상품가격, 배송비, 이익금
product_price = []
ship_price = []

for case in range(N):
    price, ship = map(int, input().split())
    product_price.append(price)
    ship_price.append(ship)

result = product_price[0]
max_benefit = 0
for i in range(len(product_price)):
    fix_price = product_price[i]
    benefit =  get_benefit(fix_price, product_price, ship_price)

    if benefit > max_benefit :
        max_benefit = benefit
        result = fix_price
    # 같은 이익이라면 더 작은 판매금액 출력
    elif benefit == max_benefit:
        result = result if result < fix_price else fix_price

# 이익이 안나는 경우 0 출력
result = result if max_benefit > 0 else 0
print(result)



