# [해결전략]
# B-> A로 역 연산을 수행하면 될 것 같다. 
# B가 1로끝나면 전 연산은 1을 붙히는 연산이고 B가 짝수라면 전 연산은 2를 곱했을 연산이니까

A,B = map(int, input().split())

cnt = 1
while B > A:
    if B%10 == 1:
        B = int(B/10)
        cnt+=1

    elif B%2 == 0:
        B = int(B/2)
        cnt+=1
    else:
        break

if B == A:
    print(cnt)
else:
    print(-1)
