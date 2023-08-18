import sys
input = sys.stdin.readline

m, n, k = map(int, input().strip().split())
secret = list(map(int, input().strip().split()))
buttons = list(map(int, input().strip().split()))

if len(buttons) < len(secret):
    print("normal")
else:
    matched = None
    for i in range(len(buttons)-len(secret)):
        matched = True
        for j in range(len(secret)):
            if buttons[i+j] != secret[j]:
                matched = False
                break
        if matched:
            break
    if matched:
        print("secret")
    else:
        print("normal")