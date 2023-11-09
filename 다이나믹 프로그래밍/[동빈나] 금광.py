t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    matrix = []

    array = list(map(int, input().split()))
    while array:
        matrix.append(array[:m])
        array = array[m:]

    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        dp[i][0] = matrix[i][0]

    for i in range(1, m):
        for j in range(n):
            print(j,i)
            dp[j][i] = matrix[j][i] +dp[j][i-1]
            if j-1 >= 0:
                dp[j][i] = max(dp[j][i], matrix[j][i] + dp[j-1][i-1])
            if j+1 < n:
                dp[j][i] = max(dp[j][i], matrix[j][i] + dp[j+1][i-1])
    
    
