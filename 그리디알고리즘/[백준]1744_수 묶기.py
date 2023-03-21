N = int(input())
inputs = []
for i in range(N):
    inputs.append(int(input()))

inputs.sort()

result = 0
for i in range(0, len(inputs), 2):
    if i == len(inputs)-1:
        result += inputs[i]
        break

    value = inputs[i]*inputs[i+1]
    if value > 0:
        result += value
    elif value == 0:
        if inputs[i] < 0:
            result += 0
        else:
            result += inputs[i+1]
    else: 
        # 부호가 바뀌는 시점
        result += inputs[i]
        result += inputs[i+1]

        # 인덱스 i+1부터 N-1까지 홀수라면..
        if (N-1-(i+1)+1) % 2 != 0:
            result += i+2
            i+=1
print(result)