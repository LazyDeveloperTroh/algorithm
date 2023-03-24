N, M = map(int, input().split())
arrays = list(map(int, input().split()))

start = 0
end = max(arrays)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    for l in arrays:
        if l > mid:
            total += (l-mid)

    if total < M:
        end = mid-1
    else:
        result = mid
        start = mid +1

print(result)
