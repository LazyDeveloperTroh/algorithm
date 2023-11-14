# 1. id 리스트의 수만큼 set을 만든다.
# 2. 유저별로 신고한 유저를 set에 담는다(set이니까 중복이 안되겠지)
# 3. 전체 set을 탐색하면서 k회 이상 신고된 유저를 찾아 정지시킨다.
# 4. set을 탐색하면서 정지된 유저가 있는지 확인한다.
def solution(id_list, report, k):
    # 유저가 신고한 정보
    userReportMap = {}
    for id in id_list:
        userReportMap[id] = set()

    # u1 신고한 유저, u2 신고당한 유저
    for i in range(len(report)):
        u1, u2 = report[i].split()
        userReportMap[u1].add(u2)

    # 정지되는 유저 찾기(자기 자신을 신고한 경우는 없음)
    stopUser = set()
    for id in id_list:
        cnt = 0
        for m in userReportMap.values():
            if id in m:
                cnt += 1
        if cnt >= k:
            stopUser.add(id)
    
    # 자신이 신고한 유저가 정지되었는지 확인
    answer = []
    for id in id_list:
        cnt = 0
        for u in userReportMap[id]:
            if u in stopUser:
                cnt += 1
        answer.append(cnt)
    return answer

print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
