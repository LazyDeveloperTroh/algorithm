import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
INF = int(1e9)
distance = [INF] * (v+1)
visited = [False] * (v+1)

for _ in range(e):
    # a에서 b는 가중치 c
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []

    # 시작점은 가중치 0
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        # 최단거리가 거리가 가장 짧은  노드 취득
        dist, now = heapq.heappop(q)

        # 이미 방문했던 노드라면 무시한다.
        if visited[now] == True:
            continue
        
        # 방문처리
        visited[now] = True

        # start→j로 이동거리보다 start→now→j로 이통했을 때 거리가 더 짧다면 거리를 갱신한다
        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

dijkstra(start)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])