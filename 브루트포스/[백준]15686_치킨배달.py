# [해결전략]
# 전체 치킨집에서 M 개를 조합하여 모든 경우의 수를 구함
# 각 경우의 수의 동네치킨거리를 구한 후 최소값을 구함

def get_combination(arr, n):
    result = []

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        el = arr[i]
        rest_arr = arr[i+1:]
        for C in get_combination(rest_arr, n-1):
            result.append([el]+C)
    return result

def get_distance(p1, p2):
    return abs(p2[0]-p1[0])+abs(p2[1]-p1[1])

N, M = map(int, input().split())

pos = []
for i in range(N):
    pos.append(list(map(int, input().split())))

# 집 위치와 치킨집 위치 
home_pos = []
chicken_pos = []
for y in range(N):
    for x in range(N):
        if pos[y][x] == 1:
            home_pos.append([y,x])
        elif pos[y][x] == 2:
            chicken_pos.append([y,x])

# 치킨집에서 M개를 선택할 때의 모든 경우의 수
chicken_combinations = get_combination(chicken_pos, M)

home_to_chicken_sum_array = []
# M개의 치킨집을 선택한 모든 경우의 수 
for chicken_combination in chicken_combinations:
    # 각집에서 최소거리인 치킨집을 선택하여 총 치킨거리를 구함
    home_to_chicken_sum = 0
    for home in home_pos:
        home_to_chicken = N*N
        for chicken in chicken_combination:
            distance = get_distance(home, chicken)
            if distance < home_to_chicken:
                home_to_chicken = distance
        home_to_chicken_sum += home_to_chicken
    home_to_chicken_sum_array.append(home_to_chicken_sum)
# 모든 경우의 수에 대해 치킨거리의 합을 구하고 그 최소값을 출력함
print(min(home_to_chicken_sum_array))