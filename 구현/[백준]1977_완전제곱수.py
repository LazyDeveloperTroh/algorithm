import math

M = int(input())
N = int(input())

sqrt_M = int(math.sqrt(M))
sqrt_N = int(math.sqrt(N))

s = sqrt_M+1 if M > sqrt_M*sqrt_M else sqrt_M
e = sqrt_N 

sum = 0
for i in range(s, e+1):
    sum += i*i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(s*s)
