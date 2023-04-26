s = int(input())
i = 1
if s == 1:
    print(1)
else:
    while True:
        if i*(i+1) == 2*s:
            break
        elif i*(i+1) > 2*s:
            i -= 1
            break
        i += 1
    print(i)
