n = int(input())
input_data = list(map(int, input().split()))
input_data.sort()

result = 0
group_count = 0
for i in input_data:
    group_count += 1
    
    if group_count >= i:
        group_count = 0
        result += 1
print(result)