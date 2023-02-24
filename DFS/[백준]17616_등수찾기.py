from sys import stdin

# N 학생, M 질문횟수, X
N, M, X = map(int, stdin.readline().split())

# 학생들의 성적 순위를 링크로 구현. 
link = [[] for _ in range(N)]
for _ in range(M):
    p1, p2 = map(int, stdin.readline().split())
    link[p2-1].append(p1-1)

# 출력. 가장높은등수 u, 가장낮은등수 v => 연결된 링크의 

