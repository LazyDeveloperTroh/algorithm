N, M = map(int, input().split())

square = []
for i in range(N):
    square.append(list(map(int,list(input()))))

for size in range(N, 1, -1):
    for i in range(0, N-size+1):
        for j in range(0, M-size+1):
            v1,v2,v3,v4 = square[i][j], square[i][j+size-1], square[i+size-1][j], square[i+size-1][j+size-1]
            if v1 == v2 and v2 == v3 and v3 == v4:
                print(size*size)
                quit()
print(1)