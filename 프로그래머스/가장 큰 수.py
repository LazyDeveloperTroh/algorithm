from functools import cmp_to_key
def compare(s1, s2):
    s1, s2 = str(s1), str(s2)
    if s1+s2 > s2+s1:
        return 1
    elif s1+s2 < s2+s1:
        return -1
    else:
        return 0


def solution(numbers):
    numbers = sorted(numbers, key=cmp_to_key(compare))
    numbers.reverse()
    numbers = list(map(str, numbers))
    answer = ''.join(numbers)
    if answer[0] == "0":
        return "0"
    return answer

print(solution([0, 0]	))