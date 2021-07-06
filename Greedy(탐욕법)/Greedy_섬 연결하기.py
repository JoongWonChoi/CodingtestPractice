###Greedy_섬연결하기###

## my algorithm ##
#섬들을 연결하는 costs중, 가장 작은 costs들의 합을 return 하도록 섬을 연결해야한다.
#섬들은 각각 번호를 지니고있는데, 섬 간의 cost를 나타내주는 costs배열에 특정 섬 a와 b에 대한 연결은 한 번만 주어진다.
#특정 섬들이 직접 연결되어있지 않을 수 있지만, 어느 섬과도 연결되지 않은 섬은 없다.
#내가 생각한 알고리즘은, 섬들을 연결한 cost를 기준으로 오름차순 정렬하여, 모든 섬들이 연결 되도록 하는 것이다.
#이 때 중요한것은, 일종의 그래프로 보았을 때 edge에 집중하기보단 node에 집중한다. 모든 node가 한 번이라도 연결이 되었다면 순회가 종료된다.
#따라서 cost기준으로 오름차순 정렬을 한 후, 가장 낮은 cost로 연결된 섬 2개를 지운다.
#이를 반복하며 모든 섬(node)가 제거되면 반복을 종료하고, cost의 합을 return한다.

##시간복잡도##
#섬의 갯수는 n개이고, 섬을 연결하는 모든 다리(edge)는 최대 n(n-1)/2개이다.
#이 알고리즘은 섬의 개수 n만큼(node)의 반복이 아니라, 섬을 연결하는 다리들(edge)을 대상으로 연산을 해야한다.
#따라서 정렬을 진행할 시, 최대 n^2 * logn^2 만큼의 시간이 소요된다.
#정렬 후 섬들에 대하여 최소값을 찾는 반복에서는, 최대 섬의 개수 n개만큼에 대하여 edge들을 탐색해야하므로 n * n(n-1)/2, 즉 최대 n^3만큼의 반복이 진행된다.
#이는 내가 했음에도 불구하고 정말 말도 안되는 효율성을 갖고있다. 다시 생각해보자 .  .  .
#worst case : O(n^3) (n=섬의 갯수)


def solution(n, costs):
    answer = 0
    #최소 cost를 갖는 섬들을 제거하기 위해 섬의 갯수 n개의 배열을 생성한다.
    islands = [0]*n
    for i in range(n):
        islands[i] = i
    #costs배열을 cost의 크기 대상으로 오름차순 정렬한다.(람다식 사용)
    costs = sorted(costs, key = lambda x:x[2])
    i = 0
    while len(islands)>0: #섬(node)들을 모두 연결하면 종료. 최소 cost로 연결된 섬들을 제거하며 모든 섬들이 제거될 때 까지.
        if costs[i][0] in islands:
            islands.remove(costs[i][0])
        if costs[i][1] in islands:
            islands.remove(costs[i][1])
        #최소 cost에 걸린 섬 두개를 각자 다른 조건문으로 탐색하고 제거한다. 그 이유는 이미 다른 최소cost다리로 연결되어 삭제된 섬이 있을 수 있기 때문이다.
        #경우에 따라 두 섬 모두 아직 연결되지 않았으면 둘 다 삭제, 둘 중 한 섬만 연결되었으면 남은 한 섬 삭제
        answer += costs[i][2]
        #최소 cost를 더한다.
        i+=1

    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n,costs))


# result : 12 / 100