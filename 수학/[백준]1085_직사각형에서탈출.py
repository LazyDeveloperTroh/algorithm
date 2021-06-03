x,y,w,h = map(int, input().split())

result = min(min(x, w-x), min(y, h-y))
print(result)