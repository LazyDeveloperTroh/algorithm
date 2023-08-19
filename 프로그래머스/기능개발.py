def solution(progresses, speeds):
    remain_days = []
    # 작업별로 기능이 완성되는데 남은 일수를 계산
    for i in range(len(progresses)):
        remainProgress = 100-progresses[i]
        remain_day = int(remainProgress // speeds[i]) if remainProgress % speeds[i] == 0 else int(remainProgress // speeds[i])+1
        remain_days.append(remain_day)
    print(remain_days)
    answer = []    
    # 배포 기준이 되는 남은날짜
    frontDays = remain_days[0] 
    # 배포되는 기능 개수
    cnt = 1 
    for i in range(1, len(remain_days)):
        # 뒤의 기능이 먼저 완성된다면 앞의 기능과 함께 배포됨. 수량 증가
        if frontDays >= remain_days[i]:
            cnt += 1
        # 앞의 기능이 먼저완성됨. 모여있던 기능개수 add
        else:
            frontDays = remain_days[i]
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)
    return answer

#print(solution([93, 30, 55]	,[1, 30, 5]	))
#print(solution([95, 90, 99, 99, 80, 99]		,[1, 1, 1, 1, 1, 1]		))
print(solution([1, 99]	,[100,100]	))

