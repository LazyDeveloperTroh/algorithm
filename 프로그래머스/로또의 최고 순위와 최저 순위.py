# 지워진 숫자가 모두 틀린 경우로 계산했을 때가 최저순위
# 지워진 숫자가 모두 맞는 경우로 계산했을 때가 최고순위
def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    remove_cnt = 0
    min_cnt = 0
    for lotto in lottos:
        if lotto == 0:
            remove_cnt += 1
        elif lotto != 0 and lotto in win_nums:
            min_cnt += 1

    answer = [rank[min_cnt + remove_cnt], rank[min_cnt]]
    return answer