def solution(numbers, hand):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    # 패드좌표
    position = [[0,0], [0,1], [0,2],
                [1,0], [1,1], [1,2],
                [2,0], [2,1], [2,2],
                [3,0], [3,1], [3,2]]
    # 시작지점
    ls = [3,0]
    rs = [3,2]
    #[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    answer = ''
    for n in numbers:
        print(ls, rs)
        pos = [3,1] if n == 0 else position[n-1]

        if n in [1,4,7]:
            answer += 'L'
            ls = pos
        elif n in [3, 6, 9]:
            answer += 'R'
            rs = pos
        else :
            lDist = abs(pos[0]-ls[0]) + abs(pos[1]-ls[1])
            rDist = abs(pos[0]-rs[0]) + abs(pos[1]-rs[1])
            if lDist < rDist:
                answer += 'L'
                ls = pos
            elif lDist > rDist:
                answer += 'R'  
                rs = pos
            else:
                if hand == "left":
                    answer += 'L'
                    ls = pos
                else:
                    answer += 'R'
                    rs = pos
    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))