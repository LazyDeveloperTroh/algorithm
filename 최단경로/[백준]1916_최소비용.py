import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

# 그래프 초기화
graph = [[] for _ in range(n+1)]

# 출발점에서의 최단거리를 담는 리스트 초기화
distance = [INF] * (n+1)

# 방문여부를 체크하는 리스트 초기화
visited = [False] * (n+1)

# a도시에서 b도시까지 비용c
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 시작점과 도착점
start, end = map(int, input().split())


def dijkstra(start):
    q = []

    # 시작점에서의 거리는 0
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        # 이미 방문한 노드라면 무시
        if visited[now]:
            continue
        
        # 방문 처리
        visited[now] = True

        # start -> j[0] 노드의 거리와 start -> now -> j[0]의 거리를 비교하여 갱신
        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

dijkstra(start)
print(distance[end])