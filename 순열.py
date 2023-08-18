from collections import deque
def solution(bridge_length, weight, truck_weights):
    stack = deque()
    stack.append(truck_weights[0])

    answer = 1    
    i = 1
    bridge_weight = truck_weights[0]
    while i < len(truck_weights):
        v = truck_weights[i]
        print(i, v, bridge_weight, stack)

        if bridge_weight+v <= weight and len(stack) < bridge_length:
            i += 1
            stack.append(v)
            bridge_weight += v
        elif stack:
            bridge_weight -= stack.popleft()
        answer+=1
    if stack:
        answer +=1
    return answer

print(solution(2, 10, [7,4,5,6]))