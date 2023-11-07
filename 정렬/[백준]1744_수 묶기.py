n = int(input())

# 음수와 양수를 나눠서 저장
# 0은 음수로 포함시킴(음수x0은 합계에 이득이고, 양수x0은 손해이기 때문)
negative = []
positive = []
for _ in range(n):
    data = int(input())
    if data <= 0:
        negative.append(data)
    else:
        positive.append(data)

# 정렬
negative.sort()
positive.sort(reverse=True)

# 합계 계산
# 각 리스트의 길이가 홀수인 경우 sum에 더해주면됨
# [-10 -5 -3] [3 5 10] => 50 - 3 + 3 + 50
# [-10 -5 0] [1 1 10] => 50 + 0 + 12
sum = 0

# 음수- 음수*음수=양수이기 때문에 무조건 합계에 이득
if len(negative) == 0:
    sum += 0
elif len(negative) == 1:
    sum += negative[0]
elif len(negative) % 2 == 0:
    for i in range(0, len(negative), 2):
        sum += (negative[i]*negative[i+1])
else:
    for i in range(0, len(negative)-1, 2):
        sum += (negative[i]*negative[i+1])
    sum += negative[len(negative)-1]

# 양수 - 양수의 경우는 n+1은 nx1보다 합계에 이득
if len(positive) == 0:
    sum += 0
elif len(positive) == 1:
    sum += positive[0]
elif len(positive) % 2 == 0:
    for i in range(0, len(positive), 2):
        if positive[i] == 1 or positive[i+1] == 1:
            sum += (positive[i] + positive[i+1])
        else:
            sum += (positive[i]*positive[i+1])
else:
    for i in range(0, len(positive)-1, 2):
        if positive[i] == 1 or positive[i+1] == 1:
            sum += (positive[i] + positive[i+1])
        else:
            sum += (positive[i]*positive[i+1])
    sum += positive[len(positive)-1]

print(sum)