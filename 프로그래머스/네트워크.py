from collections import deque
def solution(n, computers):
    graph = [[] for i in range(n)]
    visited = [False] * n
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i].append(j)
    
    answer = 0
    for i in range(len(graph)):
        # 이미 방문한 컴퓨터라면 제외
        if visited[i] == True:
            continue
            
        q = deque()
        q.append(i)
        answer += 1
        
        while q:
            p = q.pop()
            # 방문체크 후 방문처리
            if visited[p]:
                continue
            visited[p] = True
            
            # 연결된 컴퓨터 중 미방문 처리된 컴퓨터 큐에 추가
            for link in graph[p]:
                if visited[link]:
                    continue
                q.append(link)
    return answer