alpha = [-1]*26
S = list(input())

for i in range(len(S)):
    idx = ord(S[i])-97
    if alpha[idx] != -1:
        continue
    alpha[idx] = i

for i in alpha:
    print(i, end=" ")
    
