# 데이터 입력
n = int(input())
arrays = []
for _ in range(n):
    arrays.append(input())

# sorted 함수를 이용하여 우선순위에 따라 정렬
# 1. A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
# 2. 만약 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교해서 작은 합을 가지는 것이 먼저온다. (숫자인 것만 더한다)
# 3. 만약 1,2번 둘 조건으로도 비교할 수 없으면, 사전순으로 비교한다. 숫자가 알파벳보다 사전순으로 작다.
result = []
for data in arrays:
    length = len(data)
    total = 0
    for k in list(data):
        if k.isdigit():
            total += int(k)
    
    result.append((length, total, data))
result = sorted(result, key=lambda x: (x[0], x[1], x[2]))
for i in range(len(result)):
    print(result[i][2])