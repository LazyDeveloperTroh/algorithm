n = int(input())
array = list(map(int, input().split()))
array.sort()

left = 0
right = len(array)-1
result = [left, right]
while left <= right:
    # 0에 가까운 값 갱신
    if abs(array[left]+array[right]) < abs(array[result[0]] + array[result[1]]):
        result[0] = left
        result[1] = right

    # 포인터가 겹치면 종료
    if left + 1 == right or right - 1 == left:
        break
    
    # 좌측 포인터를 움직였을 때와 우측 포인터를 움직였을 때 값 비교
    right_move = array[left] + array[right-1]
    left_move = array[left+1] + array[right]
    if abs(left_move) <= abs(right_move):
        left += 1
    else:
        right -= 1
    
print(array[result[0]], array[result[1]])