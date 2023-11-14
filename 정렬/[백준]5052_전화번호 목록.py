# 입력받은 데이터 간의 포함관계가 생기면 NO, 아니면 YES
# 순차 탐색의 경우 최대 10만X10만으로 시간초과의 가능성이 있음
# 이분 탐색으로 구현 > 시간초과, 왜지.. 리스트를 재구성하는데 오래 걸리는건가..
# >> 풀이를 보고 이해했는데 사전순 정렬의 의미를 파악했다면 쉽게 해결이 가능했다.
#    사전순으로 정렬되었다는 것은 바로 우측의 문자열과 비교했을 때 시작이 중복되지 않는다면 
#    그 이후의 것도 중첩되지 않는다는 의미이다.

from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    array = []
    for _ in range(n):
        array.append(input().strip())
    array.sort()

    # 문자열 찾기
    find_result = False
    for i in range(len(array)-1):
        if array[i+1].find(array[i]) == 0:
            find_result = True
            break
    
    if find_result:
        print("NO")
    else:
        print("YES")


# def binary_search(array, target, start, end):
#     if start > end:
#         return None
    
#     mid = (start+end) // 2
#     if array[mid].find(target) == 0:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid-1)
#     elif array[mid] < target:
#         return binary_search(array, target, mid+1, end)

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     array = []
#     for i in range(n):
#         array.append(input())
#     array.sort()

#     find_result = False
#     for i in range(len(array)):
#         if binary_search(array, array[i], 0, len(array)-2) != None:
#             find_result = True
#             break

#     if find_result:
#         print("NO")
#     else:
#         print("YES")