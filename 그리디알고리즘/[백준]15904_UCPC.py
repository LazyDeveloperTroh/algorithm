s = list(input())
ucpc = ['U','C','P','C']

cnt = 0
for i in s:
    if cnt == 4:
        break

    if ucpc[cnt] == i:
        cnt += 1

if cnt == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')
