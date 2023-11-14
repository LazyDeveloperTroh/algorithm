import sys
input = sys.stdin.readline

datas = list(map(int, input().split()))
for i in range(1, len(datas)):
    diff = datas[i]-datas[i-1]
    if diff != 1 and diff != -1:
        break

if diff == 1:
    print("ascending")
elif diff == -1:
    print("descending")
else:
    print("mixed")