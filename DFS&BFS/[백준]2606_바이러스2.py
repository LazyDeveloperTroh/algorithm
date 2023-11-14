import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
link = int(input())

# 그래프 초기화, 양방향으로 초기화가 필요함
graph = [[] for i in range(n)]
for _ in range(link):
    v1, v2 = map(int, input().split())
    graph[v1-1].append(v2-1)
    graph[v2-1].append(v1-1)

# dfs 
visited = [False]*n
result = 0
def dfs(v):
    global result

    if visited[v]:
        return
    
    visited[v] = True
    result += 1

    links = graph[v]
    for link in links:
        if not visited[link]:
            dfs(link)

# 1번 컴퓨터를 루트로 dfs 탐색
dfs(0)

# 결과출력, 1번 컴퓨터 제외하기 위해 1감소
print(result-1)