# https://www.acmicpc.net/problem/1026
# 1. a, b의 곱이 최소로 만들어지려면 한쪽에서는 최대값을 다른 한쪽에서는 최소값을 설정해야 한다.
# 2. 만약 a를 내림차순으로 정렬해서 연산한다면 각 원소에 곱해지는 값은 b를 오름차순했을 때의 값일 때 최소가 된다.
#    (문제에서 b를 정렬하면 안된다고해서 실제로 곱해지는 b의 값을 연산할 필요가 없다는 뜻이다. => 그냥 오름차순 정렬하면된다.)
# 3. 단 a를 내림차순으로 실행한 결과와 a를 오름차순으로 실행한 결과가 다를 수 있기 때문에 각 결과를 구한 후 최소값을 출력한다.

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


# a의 최대값과 b의 최소값을 곱해서 연산하는 경우
min1 = 0
a.sort(reverse=True)
b.sort()
for i in range(n):
    min1 += a[i]*b[i]

# b의 최대값과 a의 최대값을 곱해서 연산하는 경우
min2 = 0
a.sort()
b.sort(reverse=True)
for i in range(n):
    min2 += a[i]*b[i]

print(min(min1, min2))
