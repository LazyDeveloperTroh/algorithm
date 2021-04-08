# [해결전략]
# 구멍은 선인데 테이프는 길이의 개념이라서 상당히 헷갈렸다. 
# 구멍을 메꾸기 위한 테이프는 길이가 몇일까? 고민해보았다.
# 구멍의 위치가 1, 2라면 테이프 길이는 2M가 필요하다. 아니면 구멍의 위치가 1,2  5,6,7 이라면  1,2를 메꾸는 2M, 5,6,7을 메꾸는 3M가 필요하다.
# 테이프의 길이 L을 이용하여 LOOP를 사용할 수 있을 것 같다. 
# 자연수는 0부터 시작이다... 삽질을 꽤 오래했다 ㅠㅠ

N, L = map(int, input().split())
position = list(map(int, input().split()))
position.sort()

# 물이샌곳을 1로 표기
position_array = [0]*position[-1]
position_array.insert(0, 0)
for i in position:
    position_array[i] = 1

tempL = 0 # 임시 테이프 길이
cnt = 0 # 테이프 수량
for i in position_array:
    if i == 1 and tempL == 0:
        cnt+=1
        tempL = L
    if tempL != 0:
        tempL -= 1

print(cnt)
