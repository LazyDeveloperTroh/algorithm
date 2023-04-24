import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

# 가장 큰 값을 찾은 후 정렬된 갯수를 구함
maxValue = max(arr) 
maxIndex = arr.index(maxValue)
sortCnt = 1
for i in range(maxIndex-1, -1, -1):
    if arr[i] == maxValue-sortCnt:
        sortCnt += 1

# 정렬된 갯수를 뺸 나머지를 '알아서' 뽑아서 정렬함
print(n - sortCnt)