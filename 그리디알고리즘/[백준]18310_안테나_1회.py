n = int(input())
input_data = list(map(int, input().split()))

cnt_array = [0] * 100001
for i in input_data:
    cnt_array[i] += 1

current = 1 # 현재 안테나위치
left = 0 # 안테나 좌측에 있는 집의 수
right = n-left # 안테나 우측에 있는 집의 수
distance = sum(input_data) - n

while current <= 100001:
    current += 1 # 안테나 위치이동
    left += cnt_array[current-1] # 안테나 위치가 이동하면 좌측의
    right = n-left
    
    # 이전 안테나 위치가 최고효율인 경우
    if distance <= distance + left - right:
        current -= 1
        break
    else:
        distance = distance + left - right
print(current)

