INF = int(1e9)

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            graph[i][j] = INF

for k in range(0, N):
    for i in range(0, N):
        for j in range(0, N):
            # i -> j 거리와 i -> k -> j 의 거리를 비교한다.
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


for i in range(N):
    for j in range(N):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print("")