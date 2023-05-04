N = int(input())

arr = [0 for i in range(10001)]
for i in range(N):
    n = int(input())
    arr[n] += 1

for i in range(len(arr)):
    if arr[i] == 0:
        continue
    for j in range(arr[i]):
        print(i)