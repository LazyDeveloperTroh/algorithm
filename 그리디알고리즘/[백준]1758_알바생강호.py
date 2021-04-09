permutation_array = []
def permutation(array, start, end):
    if start == end:
        return permutation_array.append(array)
    for i in range(start, end+1):
        tempArray = list(array)

        temp = tempArray[i] 
        tempArray[i] = tempArray[start]
        tempArray[start] = temp

        permutation(tempArray, start+1, end)

# 사람의 수
n = int(input())

# 팁
tips = []
for i in range(n):
    tips.append(int(input()))

print(permutation_array)
