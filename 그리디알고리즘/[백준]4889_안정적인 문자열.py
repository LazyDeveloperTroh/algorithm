test_case = 1
while True:
    arr = list(input())
    if arr[0] == '-':
        break

    result = 0
    stack = []
    for s in arr:
        if s == '{':
            stack.append('{')
        else:
            if len(stack) == 0:
                result += 1
                stack.append('{')
            else:
                stack.pop()

    print('{}. {}'.format(test_case, result + len(stack)//2))
    test_case += 1
