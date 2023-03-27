N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
def binary_search(trees, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for tree in trees:
            if tree > mid:
                total += (tree-mid)
        
        if total  < target:
            end = mid-1
        else:
            if result < mid:
                result = mid
            start = mid + 1
    return result
    

result = binary_search(trees, M, start, end)
print(result)