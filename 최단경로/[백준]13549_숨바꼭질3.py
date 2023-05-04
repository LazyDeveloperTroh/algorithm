import sys
import heapq

INF = int(1e9)
MAX = 100001
visited = [False] * MAX
distance = [INF] * MAX
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [[] for _ in range(MAX)]

# n이하의 간선을 통하는 경우 *2연산이 더 작아질 수 있음
for i in range(n, 0, -1):
    if i-1 >= 0:
        graph[i].append((i-1, 1))
    if i+1 <= MAX-1:
        graph[i].append((i+1, 1))
    if i*2 <= MAX-1:
        graph[i].append((2*i, 0))

# MAX-1 까지 간선을 만들필요는 없어보인다..
for i in range(n, MAX-1):
    if i-1 >= 0:
        graph[i].append((i-1, 1))
    if i+1 <= MAX-1:
        graph[i].append((i+1, 1))
    if i*2 <= MAX-1:
        graph[i].append((2*i, 0))

def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0

    while q:
        # 가중치가 가장 짧은 노드취득
        dist, n = heapq.heappop(q)

        # 이미 방문하 노드라면 무시
        if visited[n]:
            continue
        visited[n] = True

        # start에서 i[0]까지 거리와 start에서 n을 통해 i[0]까지의 거리를 비교
        for i in graph[n]:
            cost = dist + i[1] 
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])

dijkstra(n)
print(distance[k])