def solution(n, costs):
    answer = 0
    islands = [0]*n
    for i in range(n):
        islands[i] = i
    left = 0
    while len(islands)>0:
        current = costs[left][2]
        for k in range(1,n-left):
            if current > costs[k][2]:
                current = costs[k][2]
        if costs[k][0] in islands:
            islands.remove(costs[k][0])
        if costs[k][1] in islands:
            islands.remove(costs[k][1])
        del costs[k]
        answer += current
        left+=1

    return answer




n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n,costs))