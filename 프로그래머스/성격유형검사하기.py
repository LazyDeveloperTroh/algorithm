def solution(survey, choices):
    answer = ''
    pointMap = {
        "R":0, "T":0,
        "C":0, "F":0,
        "J":0, "M":0,
        "A":0, "N":0
    }

    for i in range(len(survey)):
        surv = survey[i]
        choice = choices[i]
        
        C1, C2 = list(surv)[0], list(surv)[1]
        if choice < 4:
            pointMap[C1] += 4-choice
        elif choice > 4:
            pointMap[C2] += choice-4
        
        result1 = 'R' if pointMap['R'] >= pointMap['T'] else 'T'
        result2 = 'C' if pointMap['C'] >= pointMap['F'] else 'F'
        result3 = 'J' if pointMap['J'] >= pointMap['M'] else 'M'
        result4 = 'A' if pointMap['A'] >= pointMap['N'] else 'N'
        answer = result1 + result2 + result3 + result4
    return answer

print(solution(["TR", "RT", "TR"],[7, 1, 3]))