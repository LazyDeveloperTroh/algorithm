n = int(input())
p1, p2 = map(int, input().split(" "))
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    v1, v2 = map(int, input().split(" "))
    graph[v1].append(v2)
    graph[v2].append(v1)

visit = [False] * (n+1)

global result
result = -1

def DFS(v, target, cnt):
    if v == target:
        global result
        result = cnt
        return

    visit[v] = True
    links = graph[v]
    for link in links:
        if not visit[link]:
            DFS(link, target, cnt+1)
DFS(p1, p2, 0)
print(result)
