boards = [
    [1, 1, 1, 1, 1, 1, 0], # 0
    [0, 0, 0, 1, 1, 0, 0], # 1
    [1, 0, 1, 1, 0, 1, 1], # 2
    [0, 0, 1, 1, 1, 1, 1], # 3
    [0, 1, 0, 1, 1, 0, 1], # 4
    [0, 1, 1, 0, 1, 1, 1], # 5
    [1, 1, 1, 0, 1, 1, 1], # 6
    [0, 1, 1, 1, 1, 0, 0], # 7
    [1, 1, 1, 1, 1, 1, 1], # 8
    [0, 1, 1, 1, 1, 1, 1], # 9
]

t = int(input())
for _ in range(t):
    n1, n2 = map(int, input().split())
    
    cnt = 0
    # 자릿수에 맞는 경우 횟수 계산
    while n1 != 0 and n2 != 0:
        v1, v2 = n1%10, n2%10
        for i in range(7):
            if boards[v1][i] != boards[v2][i]:
                cnt += 1
        n1 = n1//10
        n2 = n2//10

    # 자릿수가 안맞아서 꺼져있는 불 횟수계산
    if n1 != 0 or n2 != 0:
        n = n1 if n1 != 0 else n2
        while n != 0:
            for i in boards[n%10]:
                if i == 1:
                    cnt += 1
            n = n//10
    print(cnt)