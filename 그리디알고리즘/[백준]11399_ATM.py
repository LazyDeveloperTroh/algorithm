# [해결전략]
# n번째 사람이 인출하는데 소요되는 시간 S(n)은 S(n-1)+P(n)이다.
# 문제의 정답은 S(1)+S(2)...S(n)의 최소값을 출력하는 것이다. 즉 각 항을 최소로 해야한다.
# 소요시간이 적은 순서대로 줄을서야 각 항을 최소로 할 수 있다.

# 사람 수, 각 사람별 인출시간 입력
n = int(input())
p = list(map(int, input().split()))
p.sort()

# 각 사람이 인출하는데 걸리는 시간을 리스트로 저장
sumList = [0]*n
sumList[0] = p[0]
for i in range(1,n):
    sumList[i]=sumList[i-1]+p[i]

# 총 소요시간 출력
totalSum = sum(sumList)
print(totalSum)