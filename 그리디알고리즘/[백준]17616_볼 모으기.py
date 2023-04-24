n = int(input())
balls = list(input())

countR = 0 # R을 이동시키는 경우
countB = 0 # B를 이동시키는 경우
hasR = False # 우측에 R이 있는 경우
hasB = False # 우측에 B가 있는 경우
for i in range(n-2, -1, -1):
    if balls[i+1] == 'R':
        hasR = True
    else:
        hasB = True

    if balls[i] != balls[i+1]:
        if balls[i] == 'R':
            countR += 1
        else:
            countB += 1
    else:
        if balls[i] == 'B' and hasR:
            countB += 1
        elif balls[i] == 'R' and hasB:
            countR += 1
result1 = min(countR, countB)

countR = 0 # R을 이동시키는 경우
countB = 0 # B를 이동시키는 경우
hasR = False # 우측에 R이 있는 경우
hasB = False # 우측에 B가 있는 경우
for i in range(1, n):
    if balls[i-1] == 'R':
        hasR = True
    else:
        hasB = True

    if balls[i] != balls[i-1]:
        if balls[i] == 'R':
            countR += 1
        else:
            countB += 1
    else:
        if balls[i] == 'B' and hasR:
            countB += 1
        elif balls[i] == 'R' and hasB:
            countR += 1
result2 = min(countR, countB)

print(min(result1, result2))