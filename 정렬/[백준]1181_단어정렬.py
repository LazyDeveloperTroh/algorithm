N = int(input())

result = []
for i in range(N):
    s = input()
    if s in result:
        continue
    result.append(s)

    for j in range(len(result)-1, 0, -1):
        if len(result[j]) < len(result[j-1]):
            result[j-1], result[j] = result[j], result[j-1]
        elif len(result[j]) == len(result[j-1]):
            if result[j] < result[j-1]:
                result[j-1], result[j] = result[j], result[j-1]
        else:
            break
for s in result:
    print(s)
