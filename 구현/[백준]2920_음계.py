from sys import stdin

nums = list(map(int, stdin.readline().split()))

result = ''
for i in range(7):
    if (result == '' or result == 'ascending') and nums[i] < nums[i+1]:
        result = 'ascending'
    elif (result == '' or result == 'descending') and nums[i] > nums[i+1]:
        result = 'descending'
    else:
        result = 'mixed'
print(result)
