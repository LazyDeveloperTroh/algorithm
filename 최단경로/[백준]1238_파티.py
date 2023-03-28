import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

# 간선 입력. a에서 b까지가는데 c가 걸린다
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))

    distance = [INF] * (n+1)
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)

        # 이미 처리된 노드라면
        if distance[now] < dist:
            continue
        
        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))
    return distance[end]

result = 0
for i in range(1, n+1):
    total = dijkstra(i, x) + dijkstra(x, i)
    if result < total:
        result = total
print(result)
