# K를 감소시키며 남자일경우와 여자일경우로 재귀함수로 계산?
N, M, K = map(int, input().split())

max_team = min(int(N/2), M)
result = max_team
for cnt in range(max_team, -1, -1):
    rest_human = N+M-cnt*3
    if rest_human >= K:
        result = cnt
        break
print(result)

# n 여자, m 남자, k 인턴 > 시간초과
# def get_team_count(n, m, k):
#     result = []

#     if n == 0:
#         return [0]

#     if m == 0:
#         return [0]

#     if k == 0:
#         team_cnt = m if int(n/2) > m else int(n/2)
#         return [team_cnt]

#     result += get_team_count(n-1, m, k-1)
#     result += get_team_count(n, m-1, k-1)

#     return result
    
# max_team_cnt = max(get_team_count(N, M, K))
# print(max_team_cnt)

# 조합을 이용하여 K명을 선택하는 경우의 수를 구하고 최대 팀 수량을 구함 > 메모리초과
# def get_combination(arr, n):
#     result = []

#     # 종료조건
#     if n == 0:
#         return [[]]
    
#     for i in range(len(arr)):
#         el = arr[i]
#         rest_arr = arr[i+1:]

#         for C in get_combination(rest_arr, n-1):
#             result.append(C+[el])
#     return result

# N, M, K = map(int, input().split())

# # 여자는 0, 남자는 1로 초기화
# member = [0]*N
# member = member + [1]*M

# k_combinations = get_combination(member, K)

# max_team = 0
# for k_combination in k_combinations:
#     # K 명중 남자와 여자를 카운팅하여 몇개의 팀이 만들어지는지 확인
#     woman = 0
#     man = 0
#     for sex in k_combination:
#         if sex == 0:
#             woman += 1
#         else:
#             man += 1
#     team_cnt = M-man if int((N-woman)/2) > (M-man) else int((N-woman)/2)
#     # 최대 팀 수를 구함
#     if team_cnt > max_team:
#         max_team = team_cnt
# print(max_team)