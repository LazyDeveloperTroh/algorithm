from collections import deque

input_datas = list(map(int, input().split()))
k = int(input())

if k > sum(input_datas):
    print(-1)
else:
    queue = deque()
    for i in range(len(input_datas)):
        queue.append([i, input_datas[i]])

    while queue and k > 0:
        q = queue.popleft()
        idx, food_time = q[0], q[1]
        
        k -= 1
        food_time -= 1

        if food_time != 0:
            queue.append(food_time)

    idx, food_time = queue.popleft()
    print(idx)