def dfs(graph, n, cnt):
    result = []
    if n == len(graph):
        return [cnt]
    else:
        link = graph[n]
        for v in link:
            sum = dfs(graph, n+1, cnt+v)
            result += sum
    return result
     

def solution(numbers, target):
    graph = []
    for i in range(len(numbers)):
        graph.append([numbers[i], numbers[i]*-1])

    answer = 0
    result = dfs(graph, 0, 0)
    for r in result:
        if target == r:
            answer += 1
    return answer

print(solution([1, 2]	,3))
print(solution([1, 1, 1, 1, 1]	,3))
print(solution([4, 1, 2, 1]		,4))
