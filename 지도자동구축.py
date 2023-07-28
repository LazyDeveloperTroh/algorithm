import sys
input = sys.stdin.readline

N = int(input())

def f(x):
    if x == 1:
        return 3
    return f(x-1)*2-1
print(f(N)**2)
