import sys
input = sys.stdin.readline

n = int(input().strip())
bulb = list(map(int, list(input().strip())))
target = list(map(int, list(input().strip())))

# 처음 전구의 상태를 target과 동일하게 만드는 함수
INF = int(1e9)
def change(bulb, target):
    copy_bulb = bulb[:]
    cnt = 0
    
    # 두번째 인덱스부터 앞의 전구가 target과 같은지 비교
    for i in range(1, n):
        if copy_bulb[i-1] == target[i-1]:
            continue
        # 앞의 전구가 target과 다르다면 반전처리
        cnt += 1
        for j in range(i-1, i+2):
            if j < n:
                copy_bulb[j] = 1-copy_bulb[j]
    # 변환결과 리턴    
    return cnt if copy_bulb == target else INF

# 맨 처음 전구를 누르지 않았을 때 결과
result = change(bulb, target)

# 맨 처음 전구를 눌렀을 때 결과
bulb[0] = 1 - bulb[0]
bulb[1] = 1 - bulb[1]
# 이미 처음의 전구를 눌렀기 때문에 1을 더함
result = min(result, change(bulb, target)+1)

# 결과출력
if result == INF:
    print(-1)
else:
    print(result)