def solution(clothes):
    clothMap = {}
    for name, ty in clothes:
        if clothMap.get(ty) == None:
            clothMap[ty] = 1
        else:
            clothMap[ty] += 1

    answer = 1
    types = list(clothMap.values())
    for cnt in types:
        answer = answer * (cnt+1)
    return answer-1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	))