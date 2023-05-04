n = int(input())
input_datas = list(map(int, input().split()))

input_datas.sort()

n = 1
for i in input_datas:
    if n < i:
        break
    else:
        n+=i
print(n)