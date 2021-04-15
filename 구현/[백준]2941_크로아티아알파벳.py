s = input()

alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
while len(s) > 0:
    c1 = s[0:2]
    c2 = s[0:3]

    hasMatch = False
    for match in alpha:
        if c1 == match:
            s = s[2:]
            hasMatch = True
            break
        elif c2 == match:
            s = s[3:]
            hasMatch = True
            break
    
    if hasMatch == False:
        s = s[1:]
        
    cnt+=1
print(cnt)