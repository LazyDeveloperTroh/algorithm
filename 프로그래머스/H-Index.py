def solution(citations):
    citations.sort()

    # n회 미만으로 인용된 논문의 수
    under_cnt = 0

    for i in range(max(citations)+1):
        cnt = len(citations) if i == 0 else len(citations) - under_cnt
        if cnt >= 



    # {인용횟수, 논문의수}
    citations_dict = {}
    for c in citations:
        if citations_dict.get(c) == None:
            citations_dict[c] = 1
        else:
            citations_dict[c] += 1

    citations_list = list(citations_dict.keys())
    citations_list.sort()

    answer = 0
    # n회 미만으로 인용된 논문의 수
    under_cnt = 0
    for i in range(10000):
        n = citations_list[i]
        
        # n회이상으로 인용된 논문수 = 전체 논문수 - n회미만 인용된 논문수
        cnt = len(citations) if i == 0 else len(citations) - under_cnt
        
        if cnt >= n:
            answer = n
        under_cnt += citations_dict[n]
    return answer


#print(solution([3, 0, 6, 1, 5]	))
#print(solution([1, 2, 3, 4, 5]	))
#print(solution([ 1,3,9,7,2,8,5,6,4,0] 	))
print(solution([ 0,5,6,7,8] 	))