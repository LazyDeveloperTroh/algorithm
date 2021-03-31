# [해결전략]
# 로프 허용 무게를 내림차순 정렬함
# 로프를 1개, 2개, 3개, ...N개 사용할때 최대 무게를 구해서
# N개 사용할 때보다 N+1개 사용할 때 더 큰 무게를 들어올릴 수 있는지 확인 
#   > [반례]는 11 5 4.  N+2, N+3.. 까지 사용해야 MAX값이 나오는 경우도 있음.

N = int(input())

# 로프 허용무게
rope_weight = []
for i in range(N):
    rope_weight.append(int(input()))

# 로프 허용무게를 큰 것부터 정렬
rope_weight.sort(reverse=True)


max = rope_weight[0]
for i in range(1, N):
    if rope_weight[i]*(i+1) > max:
        max = rope_weight[i]*(i+1)

print(max)

