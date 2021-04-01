# [해결전략]
# 시간이 큰 버튼부터 처리.

cook_time = int(input())
button_time=[300, 60, 10]

if cook_time%10 != 0:
    print(-1)
else:
    for time in button_time:
        print(cook_time//time, end=" ")
        cook_time%=time