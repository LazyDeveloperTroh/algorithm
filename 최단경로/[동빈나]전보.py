import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split()) # n 노드, m 간선, c 시작노드
distance = [INF] * (n+1) # 각 노드까지의 최단거리를 담는 리스트

# 그래프 초기화
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, d = map(int, input().split())
    # a노드에서 b노드로 가는데 d만큼 걸린다.
    graph[a].append((b, d))

def dijkstra(start):
    h = []
    # 우선순위 큐에다가 가장 가까운 노드를 저장
    heapq.heappush(h, (0, start))
    # 시작점에서 시작점까지의 거리는 0
    distance[start] = 0 
    while h:
        # now = 현재노드, dist = now 노드까지의 현재 최단거리
        dist, now = heapq.heappop(h)

        # now 노드에 연결되어있는 다른 노드탐색
        for i in graph[now]:
            # now 노드를 통해 i[0] 노드까지 이동하는 거리
            cost = dist + i[1]

            # start -> i[0]로 이동하는 거리와 start -> now -> i[0]로 이동하는 거리 비교
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (cost, i[0])) 

print(distance)
dijkstra(c)
print(distance)
