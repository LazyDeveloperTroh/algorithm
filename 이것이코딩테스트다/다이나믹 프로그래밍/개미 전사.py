n = int(input())
input_data = list(map(int, input().split()))

d = [0] * n
d[0] = input_data[0]
d[1] = max(input_data[0], input_data[1])
for i in range(2, n):
    d[i] = max(d[i-2]+input_data[i], d[i-1])

print(d[n-1])