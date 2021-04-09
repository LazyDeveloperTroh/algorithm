# [해결전략]
# 횟수를 최소한으로 해야한다.
# 높은 레벨을 적게 수정해야 전체 변경횟수를 최소화 할 수 있다.

N = int(input())

level_score = []
for i in range(N):
    level_score.append(int(input()))

cnt = 0
for i in range(len(level_score)-1, 0, -1):
    a = level_score[i]
    b = level_score[i-1]

    while a <= b:
        b-=1
        cnt += 1 

    level_score[i-1] = b

print(cnt)
    