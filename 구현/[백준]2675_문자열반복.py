from sys import stdin

T = int(stdin.readline())
for case in range(T):
    R, S = stdin.readline().split()
    R = int(R)
    str = list(S)

    result = ""
    for str in S:
        for _ in range(R):
            result += str
    print(result)
