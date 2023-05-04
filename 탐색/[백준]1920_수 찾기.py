import sys
n = int(input())
n_array = list(map(int, input().split()))
n_array.sort()

m = int(input())
m_array = list(map(int, input().split()))

def binary_search(arr, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)


for i in m_array:
    if binary_search(n_array, i, 0, len(n_array)-1) == None:
        print(0)
    else:
        print(1)
