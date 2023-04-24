t = int(input())

for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))
    
    current_price = prices[n-1]
    total_price = 0
    for i in range(n-2, -1, -1):
        if current_price > prices[i]:
            total_price += (current_price - prices[i])
        else:
            current_price = prices[i]
    print(total_price)
