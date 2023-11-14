from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    # 함수 문자열을 리스트로 저장
    p = input()
    
    # 배열을 입력받고 deque로 저장
    n = int(input())
    arrays = input().strip()
    if arrays == "[]":
        arrays = deque()
    else:
        arrays = deque(list(map(int, arrays
                                .replace("[","")
                                .replace("]", "")
                                .split(","))))

    # 입력된 함수 수행. 에러가 발생하는 경우 break
    reverseTF = False
    error = False
    for i in range(len(p)):
        if p[i] == 'R':
            reverseTF = not reverseTF
        elif p[i] == 'D':
            if not arrays:
                error = True
                break
            else:
                if reverseTF:
                    arrays.pop()
                else:
                    arrays.popleft()
    
    # 결과 출력
    if error:
        print("error")
    else:
        if reverseTF:
            arrays.reverse()
            
        print("[", end="")
        for i in range(len(arrays)):
            if i != len(arrays)-1:
                print(arrays[i], end=",")
            else:
                print(arrays[i], end="")
        print("]")