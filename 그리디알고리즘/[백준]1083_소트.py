# [해결전략]
# 맨 앞 자리를 가장 크게 만들면 될 것 같다.
# 이동 횟수가 남는다면 다음 자리수를 가장 크게 만들면 된다.

N = int(input())
arr = list(map(int, input().split()))
S = int(input())

# 시작점과 끝점 사이에서 최고값의 인덱스를 리턴
def getMaxValueIdx(startIdx, moveCnt, arr):
    maxIdx = startIdx
    
    for i in range(startIdx, startIdx+moveCnt):
        if arr[maxIdx] < arr[i+1]:
            maxIdx = i+1
    return maxIdx    
    
startIdx = 0
while S > 0:
    # 시작점에서 몇번 이동할 수 있는지 구하고, 이동 범위 내 최고값이 있는 인덱스를 취득
    moveCnt = len(arr)-1-startIdx if S > len(arr)-1-startIdx else S
    maxIdx = getMaxValueIdx(startIdx, moveCnt, arr)
    
    if moveCnt == 0:
        break

    # 시작점이 최고값이라면 시작점 이동
    if startIdx == maxIdx:
        startIdx += 1
        continue

    # 최고값이 있는 인덱스를 시작점으로 이동시킴
    for i in range(maxIdx, startIdx, -1):
        temp = arr[i-1]
        arr[i-1] = arr[i]
        arr[i] = temp
        S -= 1
    startIdx += 1

for v in arr:
    print(v, end=" ")