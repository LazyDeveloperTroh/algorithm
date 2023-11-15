n = int(input())
arrays = list(map(int, input().split()))

# 결과 리스트
result = [0] * n

# (좌표, 인덱스) 구조로 만들고 좌표순으로 정렬
sort_arrays = []
for i in range(len(arrays)):
    sort_arrays.append((arrays[i], i))
sort_arrays.sort()

# 정렬된 리스트의 인덱스는 자기보다 작은 숫자의 수와 같다.
# 다만 중복되는 수가 있을 수 있기 때문에 중복수만 계산하여 결과 리스트에 저장한다.
duplicate = 0
result[sort_arrays[i][1]] = 0
for i in range(1, len(sort_arrays)):
    # 중복수인 경우
    if sort_arrays[i][0] == sort_arrays[i-1][0]:
        duplicate += 1
    
    # 나보다 낮은 수의 갯수 - 중복된 수의 갯수
    result[sort_arrays[i][1]] = i-duplicate

for a in result:
    print(a, end=" ")
