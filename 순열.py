def permutation(arr, n):
    result = []
    if n == 0:
        return [[]]
    elif n == 1:
        return [[i] for i in arr]
    elif n >= 2:
        for i in range(len(arr)):
            elem = arr[i]
            p = permutation(arr[:i] + arr[i+1:], n-1)
            for rest in p:
                result.append([elem]+rest)
    return result

# [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
print(permutation([1,2,3], 2))
# [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]]
print(permutation([1,2,3,4], 2))

from itertools import permutations
# [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
print(list(permutation([1,2,3], 2)))
# [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]]
print(list(permutation([1,2,3,4], 2)))