def comb(arr, n):
    result = []
    if n == 0:
        return [[]]
    elif n == 1:
        return [[i] for i in arr]
    elif n >= 2:
        for i in range(len(arr)):
            el = arr[i]
            p = comb(arr[i+1:], n-1)
            for rest in p:
                result.append([el]+rest)
    return result

def solution(clothes):
    clothMap = {}
    for name, ty in clothes:
        if clothMap.get(ty) == None:
            clothMap[ty] = 1
        else:
            clothMap[ty] += 1
    
    answer = 0
    types = list(clothMap.keys())
    for i in range(1, len(types)+1):
        results = comb(types, i)
        for result in results:
            cnt = 1
            for r in result:
                cnt *= clothMap[r]
            answer += cnt
    return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	))