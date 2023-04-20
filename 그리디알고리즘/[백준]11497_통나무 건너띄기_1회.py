t = int(input())

for _ in range(t):
    n = int(input())
    heights = list(map(int, input().split()))
    heights.sort()

    arr = [0]*n

    # 투 포인터
    start = 0
    end = n-1
    for i in range(0, n):
        if i % 2 == 0:
            arr[start] = heights[i]
            start += 1
        else:
            arr[end] = heights[i]
            end -= 1
    
    result = 0
    for i in range(1, n):
        result = max(result, abs(arr[i]-arr[i-1]))
    print(result)
