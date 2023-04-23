fib = []
fib.append(0)
fib.append(1)
i = 2
while True:
    v = fib[i-2] + fib[i-1]
    if v <= 1000000000:
        fib.append(v)
    else:
        break
    i += 1

fib.sort(reverse=True)

t = int(input())
for _ in range(t):
    result = []
    n = int(input())
    for f in fib:
        if f <= n:
            n -= f
            result.append(f)
        if n == 0:
            break

    result.sort()
    for r in result:
        print(r, end=" ")
    print("")

    