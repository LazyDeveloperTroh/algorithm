import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

# 제한속도 큐
limitQueue = deque()
for _ in range(N):
    len, spd = map(int, input().split())
    limitQueue.append((len, spd))

# 실제 데이터 큐
dataQueue = deque()
for _ in range(M):
    len, spd = map(int, input().split())
    dataQueue.append((len, spd))

# 최대속도차이
maxDiff = 0

limitLen, limitSpd = limitQueue.popleft()
dataCursor = 0
limitCursor = limitLen

# 데이터 속도 제한속도와 비교
while dataQueue:
    len, spd = dataQueue.popleft()
    dataCursor += len

    # 현재 구간이 제한 구간을 넘어간 경우
    while dataCursor > limitCursor:
        diff = spd - limitSpd
        maxDiff = diff if diff >= maxDiff else maxDiff
        if limitQueue:
            limitLen, limitSpd = limitQueue.popleft()
            limitCursor += limitLen
    
    # 현재 구간이 제한 구역에 포함된 경우
    diff = spd - limitSpd
    maxDiff = diff if diff >= maxDiff else maxDiff

    if dataCursor == limitCursor and limitQueue:
        limitLen, limitSpd = limitQueue.popleft()
        limitCursor += limitLen


print(maxDiff)
