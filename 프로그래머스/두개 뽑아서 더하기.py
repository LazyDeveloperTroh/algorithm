def comb(arr, n):
    result = []
    if n == 0:
        return [[]]
    
    if n == 1:
        return [[i] for i in arr]
    
    if n >= 2:
        for i in range(len(arr)):
            el = arr[i]
            p = comb(arr[i+1:], n-1)
            for rest in p:
                result.append([el]+rest)
    return result
    
def solution(numbers):
    result = comb(numbers, 2)
    print(result)
    answer = []
    return answer

print(solution([2, 1,3,4,1]))