# [해결전략]
# 팁을 내림차순으로 정렬하는 것이 가장 베스트가 아닐까?

# 사람수
N = int(input())

tips = []
for i in range(N):
    tips.append(int(input()))

tips.sort(reverse=True)
print(tips)

sum = 0
for i in range(len(tips)):
    tip = tips[i] - i
    if tip > 0:
        sum += tip
print(sum)
