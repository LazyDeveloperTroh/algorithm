import sys
input = sys.stdin.readline

def convertToMinutes(timeStr):
    hour, minutes = map(int, timeStr.split(":"))
    return hour*60 + minutes

totalWorkingTime = 0
for i in range(5):
    startStr, endStr = input().split()
    workingTime = convertToMinutes(endStr) - convertToMinutes(startStr)
    totalWorkingTime += workingTime
print(totalWorkingTime)    
