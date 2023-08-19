# 끝나는 점을 기준으로 내림차순 정렬
# 좌표를 이동하며 요격횟수를 계산하다가 이전보다 감소하는 구간이 최대요격수
def solution(targets):
    targets.sort(key=lambda x:[x[1], x[0]])
    print(targets)

    answer = 0 
    pos = targets[0][0]
    cnt = 0
    for i in range(1, len(targets)):
        x1, x2 = targets[i][0], targets[i][1]
        if pos > x1 and pos < x2:
            cnt += 1
        else:
            pos = targets[i][0]
        

    return answer

print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]	))