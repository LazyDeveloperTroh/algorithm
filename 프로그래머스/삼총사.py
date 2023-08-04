def combination(arr, n):
    result = []
    if n == 0:
        return [[]]
    
    if n == 1:
        return [[i] for i in arr]
    
    if n >= 2:
        for i in range(len(arr)):
            el = arr[i]
            c = combination(arr[i+1:], n-1)
            for rest in c:
                result.append([el]+rest)
    return result

def solution(number):
    answer = 0
    results = combination(number, 3)
    for r in results:
        if sum(r) == 0:
            answer += 1
    return answer

print(solution([-2, 3, 0, 2, -5]))
print(solution([-3, -2, -1, 0, 1, 2, 3]))
print(solution([-1, 1, -1, 1]))