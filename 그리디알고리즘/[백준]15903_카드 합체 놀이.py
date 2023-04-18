from queue import PriorityQueue

n, m = map(int, input().split())

cards = list(map(int, input().split()))

que = PriorityQueue()
for i in cards:
    que.put(i)

while m > 0:
    n1 = que.get()
    n2 = que.get()
    que.put(n1+n2)
    que.put(n1+n2)
    m -= 1

print(sum(list(que.queue)))