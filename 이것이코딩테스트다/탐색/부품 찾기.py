N = int(input())
N_arr = list(map(int, input().split()))
M = int(input())
M_arr = list(map(int, input().split()))

N_arr.sort()
M_arr.sort()

def binary_search(arr, target, start, end):
    if start > end:
        return None
    
    mid = (start+end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)

for i in M_arr:
    if binary_search(N_arr, i, 0, N-1) == None:
        print("no", end =" ")
    else:
        print("yes", end=" ")