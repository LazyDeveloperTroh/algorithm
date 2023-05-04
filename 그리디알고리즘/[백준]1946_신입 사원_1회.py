import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    # 데이터 입력
    n = int(input())

    input_data = []
    for j in range(n):
        input_data.append(list(map(int, input().split())))

    # 서류 심사순으로 정렬
    input_data.sort(key= lambda x : x[0])
    # 면접심사 커트라인 순위
    rank2 = input_data[0][1]
    # 합격자수
    result = n
    for j in range(1, n):
        if rank2 < input_data[j][1]:
            result -= 1
        rank2 = min(rank2, input_data[j][1])
    print(result)