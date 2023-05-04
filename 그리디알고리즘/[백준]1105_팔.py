l, r = input().split()
l = list(l)
r = list(r)

def changeAndCompare(i, l, r):
    temp = l[:]
    temp[i] = '9'
    for j in range(i+1, len(temp)):
        temp[j] = '0'

    return int("".join(temp)) <= int("".join(r))

if len(l) < len(r):
    print(0)
else:
    result = 0
    for i in range(len(l)):
        if l[i] == '8':
            changeable = changeAndCompare(i, l, r)
            if changeable:
                break
            else:
                result +=1
    print(result)
