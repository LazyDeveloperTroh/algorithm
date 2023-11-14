import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())

roomDict = {}
for _ in range(n):
    # 회의실 회의시간 초기화
    name = input().strip()
    roomDict[name] = []

for _ in range(m):
    n, start, end = input().strip().split()
    start, end = int(start), int(end)
    roomDict[n].append([start, end])

# 회의실 이름 오름차순
room_names = list(roomDict.keys())
room_names.sort()

for i, name in enumerate(room_names):
    times = roomDict[name]
    times.sort(key=lambda x:x[0])
    
    result = []
    current = 9
    for start, end in times:
        if current < start:
            result.append([current, start])
        current = end
    if current < 18:
        result.append([current, 18])

    print("Room %s:" % name)
    if not result:
        print("Not available")
    else:
        print("%d available:" % len(result))
        for s, e in result:
            print("%s-%s" % (str(s).zfill(2),str(e).zfill(2)))
    
    if i != len(room_names)-1:
        print("-----")