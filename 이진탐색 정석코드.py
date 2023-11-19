# 재귀함수
def binary_search1(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search1(array, target, start, mid-1)
    else:
        return binary_search1(array, target, mid+1, end)

# 반복문
def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1

n = 10
target = 2
array = [1,2,3,4,5,6,7,8,9,10]
print(binary_search1(array, target, 0, 9))
print(binary_search2(array, target, 0, 9))
