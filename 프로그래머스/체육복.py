def solution(n, lost, reserve):
    lost1 = list(lost)
    lost1.sort()
    reserve1 = list(reserve)
    reserve1.sort()

    # 체육복을 빌릴 수 없는 학생수 카운트
    cnt1 = 0
    for l in lost1:
        # 여분의 체육복이 있지만 잃어버린 경우
        if l in reserve1:
            reserve1.remove(l)
        elif l-1 in reserve1:
            reserve1.remove(l-1)    
        elif l+1 in reserve1:
            reserve1.remove(l+1)    
        else:
            cnt1 +=1
    answer1 = n-cnt1
    lost2 = list(lost)
    lost2.sort(reverse=True)
    reserve2 = list(reserve)
    reserve2.sort(reverse=True)
    
    # 체육복을 빌릴 수 없는 학생수 카운트
    cnt2 = 0
    for l in lost2:
        # 여분의 체육복이 있지만 잃어버린 경우
        if l in reserve2:
            reserve2.remove(l)
        elif l+1 in reserve2:
            reserve2.remove(l+1)    
        elif l-1 in reserve2:
            reserve2.remove(l-1)    
        else:
            cnt2 +=1
    answer2 = n-cnt2

    return max(answer1, answer2)

print(solution(5, [4,5], [3,4]))