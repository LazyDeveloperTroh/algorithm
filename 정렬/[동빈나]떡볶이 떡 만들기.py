# n 떡의 개수, m 떡의 길이
n, m = map(int, input().split())
heights = list(map(int, input().split()))

start = 0
end = max(heights)

result = 0
while start <= end:
    total = 0
    mid = (start+end) // 2
    for h in heights:
        if h - mid > 0:
            total += (h-mid)
    
    if total < m:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

    print(start, end)

print(result)