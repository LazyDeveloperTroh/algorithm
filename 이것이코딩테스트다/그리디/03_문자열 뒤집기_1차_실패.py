# 접근 방식은 비슷하지만 구현을 너무 못한다...ㅠㅠ
# s = list(map(int, list(input())))

# isSame = True
# result0 = 0
# for i in range(1, len(s)):
#     if s[0] != s[i]:
#         isSame = False
#     else:
#        if not isSame:
#           isSame = True
#           result0 += 1

# isSame = False
# result1 = 1
# if s[0] == 0:
#    s[0] = 1
# else:
#    s[0] = 0

# for i in range(1, len(s)):
#     if s[0] != s[i]:
#         isSame = False
#     else:
#        if not isSame:
#           isSame = True
#           result1 += 1

# print(min(result0, result1))

s = list(map(int, list(input())))
count0 = 0  # 모두 0으로 바꾸는 경우
count1 = 0 # 모두 1로 바꾸는 경우

if s[0] == 0:
    count1 += 1
else:
    count0 += 1

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == 0:
            count1 += 1
        else:
            count0 += 1
print(min(count0, count1))