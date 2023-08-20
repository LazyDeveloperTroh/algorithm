k, p, n = map(int, input().split())

result = k*p
for i in range(n-1):
    result = result%1000000007 * p%1000000007
print(result % 1000000007)