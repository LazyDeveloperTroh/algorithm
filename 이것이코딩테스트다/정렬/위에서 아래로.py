N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

def quick_sort(arr, start, end):
    if start >= end:
        return
    
    pivot = start
    left = start+1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right >= start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else :
            arr[left], arr[right] = arr[right], arr[left]
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)


quick_sort(arr, 0, len(arr)-1)
for i in arr:
    print(i, end=" ")