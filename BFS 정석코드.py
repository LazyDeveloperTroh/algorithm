from collections import deque

def bfs(graph, start, visited):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        p = q.popleft()
        print(p, end= " ")

        for i in graph[p]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
bfs(graph, 1, visited)