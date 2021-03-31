# [해결전략]
# 모든 항을 -로 만들면된다. 

# 입력받은 수식을 '-' 로 스플릿
mathExpt = input().split("-")

# 분리된 수식은 '+' 만 있는 수식인데 int로 변환하여 계산
# 문제 조건상 eval은 사용하기 어려움
for i in range(len(mathExpt)):
    addExpt = map(int,mathExpt[i].split("+"))
    mathExpt[i] = sum(addExpt)

# 계산된 항들을 - 연산함
result = mathExpt[0]
for i in range(1, len(mathExpt)):
    result -= mathExpt[i]
print(result)