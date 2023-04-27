def getSum(n):
    sum = n
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

arr = [0]*10001
for i in range(1, len(arr)):
    if arr[i] != 0:
        continue

    k = i
    while k <= 10000:
        nextK = getSum(k)
        if nextK <= 10000 and arr[nextK] == 0:
            arr[nextK] = 1
        
        k = nextK

for i in range(1, len(arr)):
    if arr[i] == 0:
        print(i)