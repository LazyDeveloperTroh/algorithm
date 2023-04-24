import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    t, s = map(int, input().split())
    arr.append((t, s))

# 종료 기한일을 기준으로 정렬
arr.sort(key= lambda x: x[1])


# 0시에 일어났을 때부터 확인
start = 0
canWork = True

# 첫번째 업무의 기한일까지만 확인하면 됨
while start <= arr[0][1]:   
    temp = start

    # 모든 업무를 처리할 수 있는지 확인
    for t, s in arr:
        if temp + t <= s:
            temp = temp + t
        else:
            canWork = False
            break
    if not canWork:
        break

    # 모든 업무를 처리할 수 있는 경우 시작 시간 증가
    start += 1

if start == 0 and canWork:
    print(-1)
else:
    print(start-1)
             
    