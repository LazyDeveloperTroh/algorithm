# 각 노드에서 다른 전체노드까지의 거리를 구하는 문제
# 처음에 DFS로 문제를 해결하려고 했지만 일부 테스트케이스에서 실패함
#   DFS로 푸는 경우 (1,2) (1,3) (2,3) 케이스의 경우 1부터 3까지의 거리가 2로 나올 수 있음
# 그래서 BFS로 문제를 풀어서 정답 판정을 받았다.
# 노드의 개수도 100개밖에 없기 때문에 플로이드워셜 알고리즘을 통해 최적화가 가능한 것을 알았다.
from collections import deque
import sys
input = sys.stdin.readline

# n 인원수, m 관계의 수
n, m = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# bfs로 target까지 최단거리 구함
def bfs(start, target, visited):
    q = deque()
    q.append((start, 0))
    visited[start] = True

    while q:
        p, cnt = q.popleft()
        if p == target:
            return cnt
        
        for i in graph[p]:
            if visited[i] == False:
                q.append((i, cnt+1))
                visited[i] = True

# 출력
result = [int(1e9)]
for i in range(1, n+1):
    total = 0
    for j in range(1, n+1):
        visited = [False]*(n+1)
        total += bfs(i, j, visited)
    result.append(total)
print(result.index(min(result)))
