from collections import deque

t = int(input())

def getMaxPriority(q):
    maxPriority = 0
    for i in range(len(q)):
        priority, idx = q[i][0], q[i][1]
        if priority > maxPriority:
            maxPriority = priority
    return maxPriority

for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    
    que = []
    for i in range(len(arr)):
        que.append([arr[i], i])
    que = deque(que)

    result = 1
    while que:
        maxPriority = getMaxPriority(que)
        priority, idx = que.popleft()
        
        # 최고 우선순위가 아니라면 맨뒤로 이동
        if priority != maxPriority:
            que.append([priority, idx])
        else:
            # 원하는 인덱스 출력 차례
            if idx == m:
                break
            result += 1
            
    print(result)