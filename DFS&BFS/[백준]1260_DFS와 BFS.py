from collections import deque

N, M, V = map(int, input().split())

# 그래프 생성
graph = [[] for i in range(N)]
for i in range(M):
    V1, V2 = map(int, input().split())
    graph[V1-1].append(V2-1)
    graph[V2-1].append(V1-1)
    # 숫자가 순서대로 방문하기 위한 정렬
    graph[V1-1].sort()
    graph[V2-1].sort()

# DFS
visited = [False]*N
def DFS(v):
    if visited[v] == True:
        return
    
    visited[v] = True
    print(v+1, end=" ")
    for link in graph[v]:
        if visited[link] == False:
            DFS(link)
DFS(V-1)
print()

# BFS
visited = [False]*N
def BFS(v):
    if visited[v] == True:
        return
    
    queue = deque()
    queue.append(v)

    while queue:
        v = queue.popleft()
        if visited[v] == True:
            continue
        
        visited[v] = True
        print(v+1, end=" ")
        for link in graph[v]:
            if visited[link] == False:
                queue.append(link)
BFS(V-1)