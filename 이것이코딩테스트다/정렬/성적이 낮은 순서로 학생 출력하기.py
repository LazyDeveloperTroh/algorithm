N = int(input())
scores = []
for i in range(N):
    name, score = input().split()
    scores.append([name, int(score)])

def quick_sort(arr, start, end):
    if start >= end:
        return
    
    pivot = start
    left = start+1
    right = end

    while left <= right:
        while left <= end and arr[left][1] <= arr[pivot][1]:
            left +=1
        while right >= start and arr[right][1] >= arr[pivot][1]:
            right -=1
        
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]
        
        quick_sort(arr, start, right-1)
        quick_sort(arr, right+1, end)

quick_sort(scores, 0, len(scores)-1)
print(scores)