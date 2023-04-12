food_times = list(map(int, input().split()))
k = int(input())

if k < len(food_times):
    print(food_times[k])
else:
    food_times.sort()

    for i in range(len(food_times)):
        # i 번째 음식을 다 먹는데 걸리는 시간
        t = food_times[i]-food_times[i-1] * (len(food_times)-i)

        if k > t:
            k -= t
        else:
            # i번째 음식을 다 먹지 못하고 k가 끝났다..?
            # 원래 음식 순서가 아니잖아.. 원래 음식 순서를 어떻게 찾지..?
            print(t)