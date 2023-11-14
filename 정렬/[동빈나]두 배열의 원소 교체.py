n, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

# arr1은 오름차순, arr2는 내림차순으로 정리
arr1.sort()
arr2.sort(reverse=True)

# arr1의 최소값을 arr2의 최대값과 swap
for i in range(k):
    if arr1[i] < arr2[i]:
        arr1[i], arr2[i] = arr2[i], arr1[i]

print(sum(arr1))