# [해결전략]
# 한 세트에 0~9까지 카드가있다.
# 6과 9는 같다고 생각한다.
# -> 6,9를 제외한 숫자 중 최대수량 카드의 수량만큼 카드세트가 필요하다.
# -> 만약 6,9가 최대수량의 카드라면 6,9를 제외한 최대카드 수량과 비교해야한다.

card_cnt = [0]*10
N = input()

for i in map(int, list(N)) :
    card_cnt[i]+=1

# 6과 9의 카드수량을 더하고 이 값이 최대일 때 카드팩의 수량을 구함
cnt69 = int((card_cnt[6]+card_cnt[9]+1)/2)

# 6과 9 를 제외하고 최대수량을 구함 = 카드팩의 수량
card_cnt[6]=0
card_cnt[9]=0
maxCnt = max(card_cnt)

if maxCnt > cnt69:
    print(maxCnt)
else:
    print(cnt69)