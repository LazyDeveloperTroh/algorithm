# n 길이, s 부분합
n, s = map(int, input().split())

arrays = list(map(int, input().split()))

length = int(1e9)
start = 0
end = 0
# 첫번째 원소가 s와 같을 때, 더이상 이후 리스트를 탐색할 필요가 없다.
if arrays[start] == s:
    length = 1
# 리스트의 전체합이 s일 때, 부분합을 구할 필요가 없다.
elif sum(arrays) == s:
    length = n
else:
    # 초기는 0부터 0까지의 합
    total = arrays[0]
    while start <= end:
        # 부분합이 s와 같다면 부분합의 길이를 재계산하고 end를 이동한다.
        if total == s:
            length = min(length, end-start+1)
            end += 1
            if end >= n:
                break
            total += arrays[end]
        # 부분합이 s보다 크다면 부분합의 길이를 재계산하고 start를 이동하여 부분합을 감소시킨다.
        elif total > s:
            length = min(length, end-start+1)
            total -= arrays[start]
            start += 1
        # 부분합이 s보다 작다면 end를 이동하여 부분합을 증가시킨다
        else:
            end += 1
            if end >= n:
                break
            total += arrays[end]
# 출력부분
if length == int(1e9):
    print(0)
else:
    print(length)
