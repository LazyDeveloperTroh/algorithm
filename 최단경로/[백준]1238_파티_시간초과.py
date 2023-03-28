import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
# 간선 입력. a에서 b까지가는데 c가 걸린다
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 방문하지 않은 노드중 거리가 가장 가까운 노드 취득
def get_smallest_node(distance, visited):
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

# min(n to x + x to n)
def dijkstra(start, end):
    visited = [False] * (n+1)
    distance = [INF] * (n+1)

    # 시작점 방문 처리
    visited[start] = True
    # 자기 자신까지의 시간 0
    distance[start] = 0
    
    for j in graph[start]:
        distance[j[0]] = j[1]
    
    for i in range(n-1):
        now = get_smallest_node(distance, visited)
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
    return distance[end]

result = 0

for i in range(1, n+1):
    total = dijkstra(i, x) + dijkstra(x, i)
    if result < total:
        result = total
print(result)
