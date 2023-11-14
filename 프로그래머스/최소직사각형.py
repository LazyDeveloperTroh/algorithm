# 1. 가로, 세로 각각의 값은 의미가 없다.
# 2. 현재 지갑의 작은 변과 큰 변을 기준으로 다음 직사각형을 비교하고 담을 수 없는 경우 지갑의 크기를 변경한다.
def solution(sizes):
    answer = 0
    
    minV, maxV = min(sizes[0][0], sizes[0][1]), max(sizes[0][0], sizes[0][1])
    for i in range(1, len(sizes)):
        w, h = sizes[i][0],  sizes[i][1]
        if minV >= min(w, h) and maxV >= max(w, h):
                continue
        
        if min(w, h) > minV:
             minV = min(w,h)
        if max(w, h) > maxV:
             maxV = max(w,h)

    answer = minV*maxV 
    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))