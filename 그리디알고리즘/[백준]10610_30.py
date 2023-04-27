arr = list(input())
arr.sort(reverse=True)

if arr[len(arr)-1] != '0':
    print(-1)
else:
    intArray = list(map(int, arr))
    if(sum(intArray) % 3 == 0):
        print(''.join(arr))
    else:
        print(-1)
