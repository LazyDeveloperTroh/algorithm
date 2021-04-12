# [해결전략]
# 주식의 최대 이익이 얼마나 되는지 계산하는 문제..
# 각 거래일에 매수해서 어떤날에 매도하면 최대의 이익금이 나오는지 
# 체크하며 이익금 누적

# 테스트케이스
test_case = int(input())

for test in range(test_case) : 
    # 거래일, 거래일동안 주가
    N = int(input())
    prices = list(map(int, input().split()))

    # 총 이익금
    total_benefit = 0
    for i in range(0, len(prices)-1):
        price = prices[i]
        max_benefit = 0
        for j in range(i+1, len(prices)):
            # i일에 매수하여 j일이 매도하였을 때 이익금. 최대 이익금을 계산하여 
            # 총 이익금에 합함
            benefit = prices[j]-prices[i]
            if benefit > max_benefit:
                max_benefit = benefit
        total_benefit += max_benefit        
    print(total_benefit)