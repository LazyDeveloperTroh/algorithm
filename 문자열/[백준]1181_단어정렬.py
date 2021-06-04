N = int(input())
datas = set()

for _ in range(N):
    s = input()
    datas.add(s)
    
result = list(datas)

# 정렬
for i in range(0, len(result)):
    for j in range(0, len(result)-1-i):
        if len(result[j]) > len(result[j+1]):
            temp = result[j+1]
            result[j+1] = result[j]
            result[j] = temp
        elif len(result[j]) == len(result[j+1]):
            j0 = list(result[j])
            j1 = list(result[j+1])
            for k in range(len(result[j])):
                if ord(j0[k]) > ord(j1[k]):        
                    temp = result[j+1]
                    result[j+1] = result[j]
                    result[j] = temp
                    break

for r in result:
    print(r, end=" ")