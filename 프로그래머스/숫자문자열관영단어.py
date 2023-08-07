def solution(s):
    wordNumberMap = {
        'zero':0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    
    for k in wordNumberMap.keys():
        s = s.replace(k, str(wordNumberMap[k]))
    answer = s
    return answer

print(solution("2three45sixseven"))