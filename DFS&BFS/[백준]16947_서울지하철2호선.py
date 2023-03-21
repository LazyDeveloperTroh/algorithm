import sys
from sys import stdin
sys.setrecursionlimit(10000)

# 순환선에 속한 역인지 확인
def init_circle_line(v, start, visited, dist):
    global circle_line
    global link
    
    visited[v] = True
    for i in link[v]:
        if i == start and dist != 1:
            circle_line[start] = True
            return
        
        if visited[i] == False:
            # 다음 링크로 이동
            init_circle_line(i, start, visited, dist+1)

def init_dist_to_circle(v, visited, dist):
    global circle_line
    global link
    global distance_to_circle

    visited[v] = True

    if circle_line[v]:
        distance_to_circle.append(dist)
        return

    for i in link[v]:
        if visited[i] == False:
            init_dist_to_circle(i, visited, dist+1)
        

N = int(stdin.readline())
link = [[] for _ in range(N)]
for i in range(N):
    data = list(map(int, stdin.readline().split()))
    link[data[0]-1].append(data[1]-1)
    link[data[1]-1].append(data[0]-1)

# 순환선 체크
circle_line = [False] * N
distance_to_circle = []

for i in range(N):
    visited = [False] * N
    init_circle_line(i, i, visited, 0)

for i in range(N):
    visited = [False] * N
    init_dist_to_circle(i, visited, 0)

for dist in distance_to_circle:
    print(dist, end=" ")