# [해결전략]
# P일중 L일만사용, V일짜리 휴가 -> L의 최대값은?
# 남은일수와 L과 비교가 핵심

df = [list(map(int, input().split()))]
while [0, 0, 0] not in df:
    df.append(list(map(int, input().split())))

for i in range(len(df)-1):
    L = df[i][0]
    P = df[i][1]
    V = df[i][2] 
    remain = V%P if V%P < L else L
    
    print('Case %d: %d'%(i+1,V//P*L+remain))

