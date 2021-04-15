# 등차수열의 합. n(a+l)/2    
# 합이 주어졌으니 a대한 식으로 변환하며 풀이

N, L = map(int, input().split())
A = 0
while L <= 100:
    if (2*N-L*L+L) % (2*L) == 0:
        A = (2*N-L*L+L)//(2*L)
        break
    L+=1

if A < 0 or L > 100:
    print(-1)
else:
    for i in range(L):
        print(A+i, end=" ")
