def solution(board, moves):
    height = [0] * len(board)
    
    for j in range(len(board)):
        for i in range(len(board)):
            if board[i][j] != 0:
                height[j] = i
                break
    
    result = []
    answer = 0
    for m in moves:
        h = height[m-1]
        if h < len(board):
            v = board[h][m-1]
            if len(result) != 0 and v == result[len(result)-1]:
                result.pop()
                answer += 2
            else:
                result.append(v)
            height[m-1] += 1
    return answer

#print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]	))
print(solution([[2,2,2,0,0],
                [2,0,0,0,0],
                [1,0,0,0,0],
                [1,0,0,0,0],
                [1,0,0,0,0]], [1,2,3,1]	))
# 3 1 2 1  12 4 1 5