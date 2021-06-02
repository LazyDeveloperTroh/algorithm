import sys
from sys import stdin
sys.setrecursionlimit(10000)

def dfs(v):
    global link
    global scores

    for i in link[v]:
        scores[i] += scores[v]
        dfs(i)

    
# 입력값 초기화
n, m = map(int, stdin.readline().split())
superior = list(map(int, stdin.readline().split()))

# 상관->부하 링크 
link = [[] * n for _ in range(n)]
for i in range(n):
    if superior[i] == -1:
        continue
    link[superior[i]-1].append(i)
    
# 각 직원의 칭찬 점수를 담을 리스트
scores = [0] * n
for _ in range(m):
    v, score = map(int, stdin.readline().split())
    # 포인트 로직. 최고 상사한테만 칭찬점수를 부여함
    scores[v-1] += score

# dfs를 1회만 실행하면서 최고상사한테 부여된 칭찬점수를 부하직원들에게 부여함
dfs(0)

for s in scores:
    print(s, end=" ")