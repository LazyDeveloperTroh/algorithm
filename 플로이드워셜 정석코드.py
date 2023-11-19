INF = int(1e9)

# 노드, 간선 입력
n = int(input())
m = int(input())

# 그래프 초기화 -출발지부터 목적지까지의 최단거리
graph = [[INF] * (n+1) for _ in range(n+1)]
# 자기 자신에서 자기 자신까지의 거리는 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] == 0

# a에서 b까지 가는 거리는 c로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 플로이드워셜 점화식
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

