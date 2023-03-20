N = int(input())
schedule = []
for i in range(N):
    schedule.append(list(map(int,input().split())))\

# 오름차순 정렬
schedule.sort()

result = []
for i in schedule:
    input_start, input_end = i[0], i[1]

    if len(result) == 0:
        result.append([input_start, input_end])
        continue
    
    # 새로운 input이 중첩되는 경우
    start, end = result[-1][0], result[-1][1]
    if input_start >= start and input_start < end:
        # 중첩이 되었을 때 종료 시간이 더 빠른 것을 기준으로 함
        if input_end < end:
            result[-1] = [input_start, input_end]
    # 중첩되지 않는 경우 append
    else:
        result.append([input_start, input_end])
print(len(result))