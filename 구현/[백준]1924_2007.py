# [해결전략]
# 2007년 1월 1일부터 2007년 n월 m일까지 총 며칠인지 알아내면됨.

# 1~12월까지 총 날짜
dates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 요일. 
# 1월1일이 월요일이니까 n월 m일까지 총 날짜의 합을 7로 나눴을 때 나머지를 인덱스로 요일을 구하면 됨
days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

# 총 날짜 구하기
sum = 0
m, d = 1, 1 
x, y = map(int, input().split())

while m < x:
    sum += dates[m-1]
    m+=1
sum += y
print(days[(sum-1)%7])
