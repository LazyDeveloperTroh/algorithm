def solution(dartResult):
    answer = 0
    bonus = {
        'S':1,
        'D':2,
        'T':3
    }
    
    scores = [0, 0, 0]
    dartResult = list(dartResult)
    score = int(dartResult.pop(0))
    i = 0
    while dartResult:
        r = dartResult.pop(0)
        if r.isdigit():
            scores[i] = score
            i += 1
            score = int(r)
        elif r in ['S', 'D', 'T']:
            score = score**bonus[r]
        elif r == '*':
            score *= 2
            if i > 0:
                scores[i-1] *= 2
        elif r == '#':
            score *= -2
        print(i, score, r)
    scores[i] = score
        
    print(scores)
    return answer
print(solution("1D2S#10S"))