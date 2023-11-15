# 두 원소의 합이 x인 조합의 수를 구하는 문제로 전형적인 투 포인터 문제
n = int(input())
arrays = list(map(int, input().split()))
x = int(input())

# 정렬 후 start는 0부터 올라가고, end는 마지막 인덱스에서부터 내려온다.
arrays.sort()
start = 0
end = len(arrays)-1
result = 0

# start는 0부터 증가하고, end는 리스트의 끝에서부터 내려온다
while start < end:
    total = arrays[start] + arrays[end]
    if total == x:
        result +=1
        end -= 1
    # 두 원소의 합이 x보다 작다면 시작점을 이동하여 합을 증가시킨다.
    elif total < x:
        start += 1
    # 두 원소의 합이 x보다 크다면 끝를 이동하여 합을 감소시킨다.
    else:
        end -= 1
print(result)