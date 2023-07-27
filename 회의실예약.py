import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dictionary = {}
for _ in range(N):
    name = input().strip()
    dictionary[name] = [0]*19

for _ in range(M):
    name, start, end = input().split()
    start = int(start)
    end = int(end)

    schedule = dictionary[name]
    for t in range(start, end):
        schedule[t] = 1

dictKeyList = sorted(list(dictionary.keys()))
for key in dictKeyList:
    schedule = dictionary[key]
    avalilable_list = []
    avalilable = []
    for i in range(9, 18):
        if schedule[i] == 0:
            avalilable.append(i)
            if i == 17:
                avalilable_list.append(avalilable)
        else:
            if avalilable:
                avalilable_list.append(avalilable)
                avalilable = []
    
    print("Room %s:" % key)
    if not avalilable_list:
        print("Not available")
    else:
        print("%d available:" % len(avalilable_list))
        for i in range(len(avalilable_list)):
            if len(avalilable_list[i]) == 0:
                continue
            print('{0:02d}'.format(min(avalilable_list[i]))+"-"+'{0:02d}'.format(max(avalilable_list[i])+1))

    if key != dictKeyList[-1]:
        print("-----")