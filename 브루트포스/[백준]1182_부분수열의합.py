cnt=0
def dfs(idx, sum):
    if idx == len(numbers):
        return

    if S == (sum+numbers[idx]): 
       global cnt
       cnt += 1
    
    dfs(idx+1, sum)
    dfs(idx+1, sum+numbers[idx])


N, S = map(int, input().split())
numbers = list(map(int, input().split()))

dfs(0,0)
print(cnt)
    

