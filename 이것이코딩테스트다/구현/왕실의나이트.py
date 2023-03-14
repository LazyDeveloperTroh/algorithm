input_data = input()
row = int(input_data[1])-1
column = int(ord(input_data[0]))-int(ord('a'))

step = [(2,1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, -2), (-1, 2)]
result = 0
for s in step:
    if (column + s[0] >= 0 and column + s[0] < 8) and (row + s[1] >= 0 and row + s[1] < 8):
        result += 1

print(result)