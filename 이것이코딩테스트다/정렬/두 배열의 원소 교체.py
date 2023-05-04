N, K = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

def quick_sort(arr, start, end):
    if start >= end:
        return
    
    pivot = start
    left = start+1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)

quick_sort(A, 0, len(A)-1)
quick_sort(B, 0, len(B)-1)

for i in range(K):
    if A[i] < B[N-1-i]:
        A[i] = B[N-i-1]
    else:
        break
print(sum(A))