# [해결전략]
# 멀티탭에 꽂혀있는 전자 제품 중 가장 나중에 사용 예정인 콘센트 구멍을 교체한다.
# 맬티탭이 비어있거나, 동일한 제품을 사용했을 때 예외처리 주의

N, K = map(int, input().split())
arr = list(map(int, input().split()))
multitab = [0 for i in range(N)]

# 멀티탭에서 사용중인 전기용품 중 가장 나중에 사용되는 전기용품의 위치를 반환
def getLastUseIndex(multitab, arr, startIdx):
    lastInfo = (0, 0) # multitab_index, distance
    for i in range(0,len(multitab)):
        # 멀티탭에서 사용중인 전기용품이 다음 사용할 때까지 거리를 계산
        distance = 0
        for j in range(startIdx, len(arr)):
            if multitab[i] != arr[j]:
                distance += 1
            elif multitab[i] == arr[j]:
                break
        if distance > lastInfo[1]:
            lastInfo = (i, distance) 
    return lastInfo[0]

i = 0
result = 0
while i < len(arr):
    # 이미 멀티탭에서 사용중이라면 다음 전기용품으로 이동
    if arr[i] in multitab:
        i+=1
    # 아직 멀티탭이 비어있다면 전기용품 할당
    elif 0 in multitab:
        emptyIndex = multitab.index(0)
        multitab[emptyIndex] = arr[i]
        i+=1
    # 멀티탭이 전부 차있다면 가장 나중에 사용하는 전기용품을 교체
    else:
        lastUseIndex = getLastUseIndex(multitab, arr, i)
        multitab[lastUseIndex] = arr[i]
        i+=1
        result +=1
print(result)