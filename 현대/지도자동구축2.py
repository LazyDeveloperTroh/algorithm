n = int(input())

def f(n):
    if n == 0:
        return 2
    return f(n-1)+2**(n-1)

print(f(1))
print(f(2))
print(f(3))
print(f(4))