# [해결전략]
# 1. 자음, 모음 최소 사용개수가 있으니까 자음과 모음을 구분하여 조합을 구한다. 2,1
# 2. 두 조합을 합친 후 오름차순 정렬한다

def get_combination(arr, n):
    result = []

    if n == 0:
        return [[]]
    
    for i in range(len(arr)):
        rest_arr = arr[i+1:]
        for C in get_combination(rest_arr, n-1):
            result.append(C+[arr[i]])
    return result

L, C = map(int, input().split())
characters = list(input().split())

# 자음, 모음을 각각 저장
jaeum_characters = []
moeum_characters = []
for c in characters:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        moeum_characters.append(c)
    else:
        jaeum_characters.append(c)

# 정답 리스트
result_array = []
# 최대 자음사용개수
jaeum_max_cnt = len(jaeum_characters)+1 if len(jaeum_characters) < L else L
for i in range(2, jaeum_max_cnt):
    # 자음, 모음 조합
    jaeum_combination = get_combination(jaeum_characters, i)
    moeum_combination = get_combination(moeum_characters, L-i)

    for j in jaeum_combination:
        for m in moeum_combination:
            jm = list(j)+list(m)
            jm.sort()
            s = ''.join(jm)
            result_array.append(s)

result_array.sort()
for result in result_array:
    print(result)