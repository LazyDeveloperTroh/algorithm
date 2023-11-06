# 순차 탐색을 하면 최대 500,000^2가 발생하기 때문에 시간 초과가 발생함
# > 정렬을 해야하나? 정렬을 했다고 하더라도 값을 비교하기 위해서는 탐색이 필요하다. 
# > 현재까지 공부한 내용으로는 해결하기가 어려워보임(그리디, DFS/BFS, 정렬)
# > 탐색을 배우고 오자!
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

cards_dict = {}
for card in cards:
    if card in cards_dict:
        cards_dict[card] += 1
    else:
        cards_dict[card] = 1

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)

result = []
cards.sort()
for target in targets:
    if binary_search(cards, target, 0, len(cards)-1) != None:
        result.append(cards_dict.get(target))
    else:
        result.append(0)

for r in result:
    print(r, end=" ")

