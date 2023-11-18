import sys
input = sys.stdin.readline

# 데이터 입력 및 초기화
k, n = map(int, input().split())
arrays = []
for _ in range(k):
    arrays.append(int(input()))

# 가장 긴 랜선의 길이를 이분탐색으로 계산하고 전체 랜선 수량을 계산한다.
start = 0
end = max(arrays)
result = 0
while start <= end:
    # 이분탐색한 길이
    mid = (start+end) // 2

    # mid가 0이라는 것은 길이가 1이라는 의미, 무조건 n개의 랜선을 만들 수 있음
    if mid == 0:
        result = max(result, mid)
        start = mid+1
        continue

    # 이분탐색한 길이로 전체 랜선을 잘랐을 때 몇개가 나오는지 계산
    total = 0
    for i in arrays:
        total += (i//mid)
    
    # 전체 랜선의 수량이 부족하면 기준랜선의 길이를 절반으로 줄이고, 수량을 넘었다면 길이를 50% 증가시킴
    if total >= n:
        result = max(result, mid)
        start = mid+1
    elif total < n:
        end = mid-1

print(result)