# [해결전략]

S = input()
T = input()

while len(T) > len(S):
    last = T[-1]
    if last == 'A':
        T = T[0:len(T)-1]
    else:
        T = T[0:len(T)-1]
        T = T[::-1]
    
if S == T:
    print(1)
else:
    print(0)


