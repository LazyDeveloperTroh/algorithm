import math
def permutation(arr, n):
    result = []
    if n == 0:
        return [[]]
    elif n == 1:
        return [[i] for i in arr]
    elif n >= 2:
        for i in range(len(arr)):
            el = arr[i]
            p = permutation(arr[:i]+arr[i+1:], n-1)
            for rest in p:
                result.append([el]+rest)
    return result

def solution(numbers):
    # 문자열을 리스트로 변환
    numbers_to_list = list(numbers)

    answer = 0
    for i in range(1, len(numbers)+1):
        # 자릿수에 맞는 순열 취득
        p = permutation(numbers_to_list, i)

        # 정수형으로 변환 후 set에 저장(중복제거)
        num_set = set()
        for result in p:
            # 0으로 시작하면 정수로 변환했을 때 순열의 길이 차이가 발생함
            if result[0] == "0":
                continue
            num_set.add(int(''.join(result)))
        
        for n in num_set:
            if n == 0 or n == 1:
                continue

            # 소수인지 확인
            isPrime = True
            for j in range(2, int(math.sqrt(n))+1):
                if n % j == 0:
                    isPrime = False
                    break
            if isPrime:
                answer +=1
    return answer


print(solution("9999999"))