def combination(arr, n) :
    result = []
    if n == 0:
        return [[]]
    
    for i in range(0, len(arr)):
        elem = arr[i]
        rest_arr = arr[i+1:]
        for C in combination(rest_arr, n-1):
            result.append([elem]+C)
    return result

heights = []
for i in range(9):
    heights.append(int(input()))

heights.sort()
heights_combinations = combination(heights, 7)
for heights_combination in heights_combinations:
    if sum(heights_combination) == 100:
        for h in heights_combination:
            print(h)
        break

