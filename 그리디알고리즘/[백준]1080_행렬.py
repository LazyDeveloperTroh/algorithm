# 행렬의 원소를 비교하고 다른 경우 반전시킴.
# 일치할 수 없다고 판단되면 -1 출력

def change(mat1, i, j):
    for n in range(3):
        for m in range(3):
            if mat1[i+n][j+m] == 0:
                mat1[i+n][j+m] = 1
            else:
                mat1[i+n][j+m] = 0


N, M = map(int, input().split())

mat1 = []
mat2 = []

for i in range(N):
    mat1.append(list(map(int, list(input()))))
for i in range(N):
    mat2.append(list(map(int, list(input()))))

cnt = 0
for i in range(N-2):
    for j in range(M-2):
        if mat1[i][j] != mat2[i][j]:
            change(mat1, i, j)
            cnt+=1

for i in range(N):
    for j in range(M):
        if mat1[i][j] != mat2[i][j]:
            print(-1)
            quit()
print(cnt)