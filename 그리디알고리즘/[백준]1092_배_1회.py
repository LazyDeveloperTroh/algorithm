import sys
input = sys.stdin.readline

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxs = list(map(int, input().split()))

cranes.sort(reverse=True)
boxs.sort(reverse=True)

if cranes[0] < boxs[0]:
    print(-1)
else:
    time = 0
    while len(boxs) > 0:
        for crane in cranes:
            for box in boxs:
                if crane >= box:
                    boxs.remove(box)
                    break
        time += 1
    print(time)

    