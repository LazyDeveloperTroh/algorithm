t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    matrix = []

    # 1차원 리스트를 2차원 리스트로 변경
    array = list(map(int, input().split()))
    while array:
        matrix.append(array[:m])
        array = array[m:]

    # DP 테이블 초기화, DP 1열 초기화
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        dp[i][0] = matrix[i][0]

    for i in range(1, m):
        for j in range(n):
            # 왼쪽에서 오는 경우
            dp[j][i] = matrix[j][i] +dp[j][i-1]
            # 왼쪽 위에서 오는 경우
            if j-1 >= 0:
                dp[j][i] = max(dp[j][i], matrix[j][i] + dp[j-1][i-1])
            # 왼쪽 아래서 오는 경우
            if j+1 < n:
                dp[j][i] = max(dp[j][i], matrix[j][i] + dp[j+1][i-1])
    
    
