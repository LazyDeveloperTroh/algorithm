s = list(map(int, list(input())))

count0 = 0 # 0으로 만들 때 횟수
count1 = 0 # 1로 만들 때 횟수

if s[0] == 1:
    count0 +=1
else:
    count1 += 1

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        if s[i] == 0:
            count1 += 1
        else:
            count0 += 1

print(min(count0, count1))