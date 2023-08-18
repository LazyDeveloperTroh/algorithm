n = int(input())

def f(n):
    if n == 0:
        return 2
    return f(n-1)+2**(n-1)
print(f(n)*f(n))