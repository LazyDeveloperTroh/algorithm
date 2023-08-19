from collections import deque

def solution(priorities, location):
    # 로케이션 별 우선순위 정보
    loc_priority = []
    for i in range(len(priorities)):
        loc_priority.append([i, priorities[i]])
    
    # 가장높은 우선순위를 비교하기위한 stack
    priorities.sort()
    prioritySortStack = deque(priorities)

    answer = 0
    q = deque(loc_priority)
    while q:
        p = q.popleft()
        loc, priority = p[0], p[1]
        maxPriority = prioritySortStack.pop()
        if priority == maxPriority:
            answer += 1
            # 찾아야하는 로케이션
            if loc == location:
                break
        else:
            # 현재 실행할 수 없는 우선순위라면 큐에 다시 저장
            q.append([loc, priority])
            # 우선순위 비교 stack 복구
            prioritySortStack.append(maxPriority)
            
    return answer

print(solution([2, 1, 3, 2]	, 2))
print(solution([1, 1, 9, 1, 1, 1]		, 0))