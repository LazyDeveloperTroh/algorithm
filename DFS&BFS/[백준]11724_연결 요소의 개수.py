import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

N, M = map(int, input().split())

graph = [[] for i in range(N)]
for i in range(M):
    v1, v2 = map(int, input().split())
    graph[v1-1].append(v2-1)
    graph[v2-1].append(v1-1)

visited = [False] * N
def dfs(v):
    if visited[v] == True:
        return
    
    visited[v] = True
    for link in graph[v]:
        if visited[link] == True:
            continue
        dfs(link)

result = 0
for i in range(N):
    if visited[i] == False:
        dfs(i)
        result += 1

print(result)
