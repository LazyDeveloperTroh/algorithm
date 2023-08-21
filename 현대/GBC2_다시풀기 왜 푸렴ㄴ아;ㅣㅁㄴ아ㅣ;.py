import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().strip().split())

# 제한구역 정보 큐에 저장
q = deque()
for _ in range(n):
    section, limit = map(int, input().strip().split())
    q.append([section, limit])

maxDiff = 0
currentHeight = 0
sectionHeight = 0
section, limit = q.popleft()
sectionHeight = section
# 관측정보 입력
for _ in range(m):
    length, speed = map(int, input().strip().split())
    currentHeight += length
    
    # 관측구역이 제한구역에 포함되어 있는 경우
    if currentHeight < sectionHeight:
        maxDiff = max(maxDiff, speed-limit)
    # 제한구역과 관측구역이 같은 높이에서 끝난 경우
    elif currentHeight == sectionHeight:
        maxDiff = max(maxDiff, speed-limit)
        if q:
            section, limit = q.popleft()
            sectionHeight += section
    # 관측구역이 제한구역을 넘어간 경우, 제한구역이 관측구역안으로 들어올때까지 loop
    else:
        while currentHeight > sectionHeight:
            maxDiff = max(maxDiff, speed-limit)
            if q:
                section, limit = q.popleft()
                sectionHeight += section
        # 이제 제한구역이 더 높아진 경우, 공통되는 구간에 대해서 max값 계산
        if sectionHeight >= currentHeight:
            maxDiff = max(maxDiff, speed-limit)
print(maxDiff)
        