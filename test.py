def solution(ingredient):
    answer = 0
    temp = []
    order = [1,2,3,1]
    
    j = 0
    while True:
        before_answer = answer
        for idx, i in enumerate(ingredient):
            if i != order[j]:
                print("#", idx, i)
                temp.append(i)
            else:
                j += 1
                if j == 4:
                    j = 0
                    answer += 1
        if before_answer == answer:
            break
        ingredient = list(temp)
        temp = []
        
    return answer

print(solution([2, -1, 1, -1, -1, -1, 2, 3, 1]))