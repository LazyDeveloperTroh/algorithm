n = int(input())
result = n
for _ in range(n):
    word = list(input())
    index = {
        "a": -1, "b": -1, "c": -1, "d": -1, "e": -1, "f": -1, "g": -1, "h": -1, "i": -1, "j": -1,
        "k": -1, "l": -1, "m": -1, "n": -1, "o": -1, "p": -1, "q": -1, "r": -1, "s": -1, "t": -1,
        "u": -1, "v": -1, "w": -1, "x": -1, "y": -1, "z": -1}


    bw = word[0]
    index[bw] = 0

    for j in range(1, len(word)):
        w = word[j]
        if w != bw and index[w] != -1:
            result -= 1
            break
        else:
            bw = w
            index[w] = j
            
print(result)
