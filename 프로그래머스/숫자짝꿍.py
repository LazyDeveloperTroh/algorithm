def solution(X, Y):
    result = ""
    
    arr1 = [0]*10
    arr2 = [0]*10
    for x in list(X):
        x = int(x)
        arr1[x] += 1
    
    for y in list(Y):
        y = int(y)
        arr2[y] += 1

    for i in range(9, -1, -1):
        minCnt = min(arr1[i], arr2[i])
        for _ in range(minCnt):
            result += str(i)
    if result == "":
        return "-1"
    if result[0] == "0":
        return "0"
    return result

print(solution("100", "203045"))