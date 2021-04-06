# [해결전략]
# 캐시를 이용하여 수행시간 감소가 포인트

fibo_array = [0, 1]
def fibo(n):
    # 피보나치 배열에 값이 없음
    if len(fibo_array) <= n:
        fibo_array.append(fibo(n-1)+fibo(n-2))
        return fibo_array[n]
    else:
        return fibo_array[n]
n = int(input())
print(fibo(n))