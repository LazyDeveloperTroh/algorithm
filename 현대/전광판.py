import sys
from collections import deque
input = sys.stdin.readline

onCnt = [6, 2, 5, 5, 4, 5, 6, 4, 7, 6]
board = [
    [1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 1, 1],
    [0, 0, 1, 1, 1, 1, 1],
    [0, 1, 0, 1, 1, 0, 1],
    [0, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1],
    [0, 1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1]
]

testCase = int(input())
for _ in range(testCase):
    queue = deque()

    n1, n2 = input().split()
    for i in range(4, -1, -1):
        digit = i+1
        if len(n1) >= digit and len(n2) >= digit:
            queue.append((int(n1[i]), int(n2[i])))
        elif len(n1) >= digit and len(n2) < digit:
            queue.append((int(n1[i]), -1))
        elif len(n1) < digit and len(n2) >= digit:
            queue.append((-1, int(n2[i])))
        else:
            queue.append((-1, -1))
    print(queue)
    
    totalCnt = 0
    if queue:
        n1, n2 = queue.popleft()
        if n1 == -1 and n2 == -1:
            continue
        else:
            if n1 == -1:
                totalCnt += onCnt[n2-1]
            elif n2 == -1:
                totalCnt += onCnt[n1-1]
            else:
                for i in range(7):
                    if board[n1-1][i] != board[n2-1][i]:
                        totalCnt += 1

    print(totalCnt)