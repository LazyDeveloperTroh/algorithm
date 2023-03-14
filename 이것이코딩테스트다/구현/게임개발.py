N, M = map(int, input().split()) # 3 <= N, M <= 50
row, column, d = map(int, input().split()) # 0 북, 1 동, 2 남, 3 서
west_pos = [(-1, 0), (0, 1), (1, 0), -1, 0] # 방향에 따른 서쪽 좌표
maps = [] # 0 육지 1 바다 
for i in range(N):    
	maps.append(list(map(int, input().split())))

result = []
def move(h, w, d, rs):
    maps[h][w] = 1
    rs.append((h, w))

    for i in range(4):
        i = (i+d) % 3
        west = west_pos[i]
        wh = h+west[1]
        ww = w+west[0]
        
        if wh >= 0 and wh <M and ww >= 0 and ww < M:
            if maps[wh][ww] == 0:
                return move(wh, ww, i, rs)
            
move(row, column, d, result)
print(len(result))