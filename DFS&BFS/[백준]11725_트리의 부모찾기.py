import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n)]
for _ in range(n-1):
    v1, v2 = map(int, input().split())
    graph[v1-1].append(v2-1)
    graph[v2-1].append(v1-1)

parents = [-1] * n
visited = [False] * n
def dfs(v):
    if visited[v]:
        return
    
    visited[v] = True
    for link in graph[v]:
        if not visited[link]:
            parents[link] = v
            dfs(link)
dfs(0)
for i in range(1, len(parents)):
    print(parents[i]+1)