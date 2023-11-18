# 초기화
n, k = map(int, input().split())
arrays = list(map(int, input().split()))

# 키 차이를 저장
diff = []
for i in range(1, n):
    diff.append(arrays[i]-arrays[i-1])

# 키 차이가 많이 발생하는 구간으로 그룹핑
diff.sort(reverse=True)
print(sum(diff[k-1:]))
