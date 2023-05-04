# n = int(input())
# input_data = list(map(int, input().split()))

# def aaa(arr, i):
#     if len(arr) == n:
#         return i
    
#     for i in range(2):
#         arr = arr + aaa(arr, n)
    

# print(aaa([], 3))

n = int(input())
input_data = list(map(int, input().split()))

target = 1
for x in input_data:
    if x > target:
        break
    else:
        target += x

print(target)   