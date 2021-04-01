# [해결전략]
# 각 알파벳 별로 합을 구한 후 계수를 취득한다.
#   > ABA = 101A+10B > 101, 10 
# 계수를 내림차순 정렬 후 9부터 곱해주면 정답을 구할 수 있다.

N = int(input())

words = []
for i in range(N):
    words.append(input())

# A-Z 까지의 계수를 담는 리스트
alpha_list = [0]*26

for word in words:
    wordToChars = list(word)  
    for i in range(0, len(wordToChars)):
        c = wordToChars[i]
        # 알파벳 계수를 저장
        alpha_list[ord(c)-65] += 10**(len(wordToChars)-1-i)

# 계수를 내림차순으로 정렬
alpha_list.sort(reverse=True)

# 높은계수부터 9~0까지 곱해줌
sum = 0
num = 9
for i in alpha_list:
    if i == 0:
        break
    sum += i*num
    num-=1

print(sum)