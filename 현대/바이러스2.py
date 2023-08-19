k, p, n = map(int, input().split())

result = k*p
for i in range(n-1):
    result = result%n * p%n
print(result % 1000000007)