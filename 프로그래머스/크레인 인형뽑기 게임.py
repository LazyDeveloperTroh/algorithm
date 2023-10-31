def solution(board, moves):
    height = [0,0,0,0,0]
    
    # 제일 높이있는 인형의 위치 계산
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 0 and height[j] == 0:
                height[j] = i

    answer = 0
    before = []
    stack = []

    for m in moves:
        h = height[m-1]
        if h < len(board):
            v = board[h][m-1]
            if not before and before[0] == v:
                before.pop()
                stack.pop()
                answer += 2
            else:
                stack.append(v)    
                before.append(v)
            height[m-1] += 1
    return answer

print(solution([[0,0,0,0,0],
                [0,0,1,0,3],
                [0,2,5,0,1],
                [4,2,4,4,2],
                [3,5,1,3,1]], [1,5,3,5,1,2,1,4]	))