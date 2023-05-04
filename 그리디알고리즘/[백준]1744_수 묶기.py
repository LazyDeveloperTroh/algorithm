import sys
input = sys.stdin.readline

N = int(input())
input_data = []
for _ in range(N):
    input_data.append(int(input()))

to_up_total = 0 # 첫번째 인덱스에서 시작한 최대값
idx = 0
while idx < N-1:
    if input_data[idx] < 0 and input_data[idx+1] < 0:
        to_up_total += input_data[idx]*input_data[idx+1]
        idx += 2
    elif input_data[idx] < 0 and input_data[idx+1] == 0:
        to_up_total += input_data[idx]*input_data[idx+1]
        idx += 2
    elif input_data[idx] <= 0 and input_data[idx+1] > 0:
        to_up_total += input_data[idx]
        idx += 1
    else:
        to_up_total += input_data[idx]*input_data[idx+1]
        idx += 2
if idx == N-1:
    to_up_total += input_data[N-1]

    
to_down_total = 0 # 마지막 인덱스에서 시작한 최대값
idx = len(input_data)
while idx > 0:
    if input_data[idx] > 0 and input_data[idx-1] > 0:
        to_down_total += input_data[idx]*input_data[idx-1]
        idx -= 2
    elif input_data[idx] > 0 and input_data[idx-1] == 0:
        to_down_total += input_data[idx]
        idx -= 1
    elif input_data[idx] < 0 and input_data[idx-1] < 0:
        to_down_total += input_data[idx]*input_data[idx-1]
        idx -= 2
if idx == 0:
    to_down_total += input_data[0]
print(max(to_up_total, to_down_total))