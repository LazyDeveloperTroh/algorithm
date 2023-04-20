import sys
input = sys.stdin.readline

n = int(input())
rank = []
for _ in range(n):
    rank.append(int(input()))
rank.sort()

temp_rank = 1
total = 0
for r in rank:
    total += abs(r-temp_rank)
    temp_rank += 1

print(total)