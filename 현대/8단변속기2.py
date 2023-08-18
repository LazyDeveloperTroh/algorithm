import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))

result = ""
for i in range(len(nums)-1):
    if nums[i+1]-nums[i] == 1:
        result = "ascending"
    elif nums[i+1]-nums[i] == -1:
        result = "descending"
    else:
        result = "mixed"
        break
print(result)
