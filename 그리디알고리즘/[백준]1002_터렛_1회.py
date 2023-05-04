# https://www.acmicpc.net/problem/1002
# 1. 원의 접점을 구하는 문제로 보인다.
# 2. 규현, 승환이 포함 관계가 아닌 경우
#    규현, 승환의 거리 == r1+r2 => 1개
#    규현, 승환의 거리 < r1+r2  => 2개
#    규현, 승환의 거리 > r1+r2  => 0개
# 3. 규현, 승환이 포함 관계인 경우
#    규현, 승환의 거리 == abs(r1-r2) => 내부접점 1개
#    규현, 승환의 거리 <  abs(r1-r2) => 0개
# 4. 같은 위치의 같은 거리인 경우 => 무한(-1)
import math

t = int(input())
input_datas = []
for _ in range(t):
    input_datas.append(list(map(int, input().split())))

for x1, y1, r1, x2, y2, r2 in input_datas:
    dist = math.sqrt(pow((x2-x1), 2) + pow((y2-y1),2))

    # 같은 원인 경우
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    # 규현이 승환에 포함된 경우
    elif dist == abs(r1-r2):
        print(1)
    elif dist < abs(r1-r2):
        print(0)
    # 포함관계가 아닌 경우
    elif dist == r1+r2:
        print(1)
    elif dist < r1+r2:
        print(2)
    elif dist > r1+r2:
        print(0)