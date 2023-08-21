def solution(clothes):
    # 의상별 수를 dictionary에 저장
    clothMap = {}
    for name, ty in clothes:
        if clothMap.get(ty) == None:
            clothMap[ty] = 1
        else:
            clothMap[ty] += 1

    # 경우의 수 계산, +1을 하는 경우는 입지 않았을 때의 경우
    answer = 1
    types = list(clothMap.values())
    for cnt in types:
        answer = answer * (cnt+1)
    
    # -1을 하는 이유는 의상을 모두 입지않은 경우제외
    return answer-1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	))