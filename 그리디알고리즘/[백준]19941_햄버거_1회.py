n, k = map(int, input().split())

arr = list(input())
visit = [False] * n

result = 0
for i in range(n-1, -1, -1):
    if arr[i] != 'P':
        continue

    match = False    
    for j in range(k, 0, -1):
        if i+j >= n or arr[i+j] != 'H':
            continue

        if visit[i+j] == False:
            visit[i+j] = True
            match = True
            result += 1
            break
    
    if match:
        continue

    for j in range(1, k+1):
        if i-j < 0 or arr[i-j] != 'H':
            continue
        
        if visit[i-j] == False:
            visit[i-j] = True
            result += 1
            break
print(result)
