from sys import stdin

N = int(stdin.readline())
A = list(map(int,stdin.readline().split()))
B, C = map(int, stdin.readline().split())


# 총 감독관은 무조건 한명씩 있어야하니까 초기값을 총 감독관으로 함
cnt = N

# 총 감독관의 감시인원을 수험생 리스트에서 제외
for i in range(len(A)):
    A[i] = A[i] - B
    
    if A[i] <= 0:
        continue
    
    if A[i]%C == 0:
        cnt = cnt + A[i]//C
    else: 
        cnt = cnt + A[i]//C + 1
print(cnt)