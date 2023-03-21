from sys import stdin

def get_distance(p1, p2, dist, visited):
    global links
    result = []

    if p1 == p2:
        return [dist]
    
    visited[p1] = True
    for link in links[p1]:
        if visited[link[0]] == False:
            result.extend(get_distance(link[0], p2, dist+link[1], visited))
    return result
                

N, M  = map(int, stdin.readline().split())

links = [[] for _ in range(N)]
for _ in range(N-1):
    p1, p2, dist = map(int, stdin.readline().split())
    links[p1-1].append([p2-1, dist])
    links[p2-1].append([p1-1, dist])

for _ in range(M):
    p1, p2 = map(int, stdin.readline().split())
    distance = get_distance(p1-1, p2-1, 0, [False]*N)
    dist = max(distance)
    print(dist)

