# dfs 이용해서 하나의 섬은 찾을 수 있는데 떨어진 섬은
# 찾을 수가 없었음. why? 링크가 끊어지기 때문에
# 그래서 시작 인덱스를 바꿔가면서 dfs 해줌
import sys
from sys import stdin
sys.setrecursionlimit(10000)

def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

# 연결방향 체크[y,x]
direct = [[-1,0], [-1,1], [0, 1], [1,1], [1,0], [1,-1], [0, -1], [-1,-1]]

while True:
    w, h = map(int, stdin.readline().split())
    if w == 0 and h == 0 :
        quit()

    map_array = []
    for i in range(h):
        map_array.append(list(map(int, stdin.readline().split())))

    # 그래프와 방문노드
    graph = []
    visited = [False] * (w*h)

    for y in range(h):
        for x in range(w):
            link = []
            # 현재 노드가 땅일 경우
            if map_array[y][x] == 1:
                # 주변 노드를 살피면서 땅이 있는 경우 링크로 연결
                for pos in direct:
                    if (y + pos[0]) >= 0 and (y + pos[0] < h) and (x + pos[1]) >= 0 and (x + pos[1] < w):
                        if map_array[y+pos[0]][x+pos[1]] == 1:
                            link_node = w*(y+pos[0]) + (x+pos[1])
                            link.append(link_node)
                # 섬이 1개의 땅으로만 이루어진 경우도 있기 때문에 현재 노드도 저장함
                now_node = w*y+x
                graph.append([now_node]+link)
            else:
                graph.append(link)
            
    cnt = 0
    for v in range(len(graph)):
        if not graph[v]:
            continue
        if visited[v] == False:
            cnt += 1
            dfs(graph, v, visited)
    print(cnt)

