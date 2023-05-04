# 20230403
# n = int(input())
# input_datas = list(map(int, input().split()))

# fears = [0] * (n+1)

# for i in input_datas:
#     fears[i] += 1

# input_datas.sort()
# result = 0

# for i in input_datas:
#     cnt = i
#     for j in range(0, i+1):
#         if fears[j] > 0 :
#             if fears[j] > cnt:
#                 fears[j] -= cnt
#                 cnt = 0
#             else:
#                 cnt -= fears[j]
#                 fears[j] = 0
#         if cnt == 0:
#             print(i, j)
#             result += 1
#             break
# print(result)

n = int(input())
input_datas = list(map(int, input().split()))
input_datas.sort()

count = 0 # 현재 그룹에 속한 인원
result = 0 
for i in input_datas:
    count += 1

    if count >= i:
        count = 0
        result += 1

print(result)
