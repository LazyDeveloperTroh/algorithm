import sys
from queue import PriorityQueue

input = sys.stdin.readline
n = int(input())
q = PriorityQueue()

for _ in range(n):
    card = int(input())
    q.put(card)


result = 0
if q.qsize() == 1:
    print(0)
else:
    while q.qsize() >= 2:
        n1 = q.get()
        n2 = q.get()
        result += (n1+n2)
        q.put(n1+n2)
    print(result)
