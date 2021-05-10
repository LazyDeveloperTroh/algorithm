from sys import stdin

n = map(int, stdin.readline().split())
m_sum = 0
for i in n:
    m_sum += i*i

print(m_sum%10)