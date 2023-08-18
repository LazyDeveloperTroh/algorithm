def solution(N, stages):
    stageCnt = [0] * (N+2)
    for s in stages:
        stageCnt[s] += 1
    
    failRate = []
    for i in range(1, N+1):
        stageUserCnt = sum(stageCnt[i:])
        if stageUserCnt == 0:
            failRate.append((i,0))
        else:
            failRate.append((i, stageCnt[i] / stageUserCnt))
    
    failRate.sort(key = lambda x:x[1], reverse=True)

    answer = []
    for idx, fr in failRate:
        answer.append(idx)
    return answer