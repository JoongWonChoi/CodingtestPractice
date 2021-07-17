###Greedy_공주님의 정원(코드업)###

## my algorithm ##
#3/1부터 11/30까지 공주님의 정원에 항상 꽃이 적어도 하나 이상 피어있도록 설계해야한다.
#이 문제는 잘 알려져있는 강의실 배정 문제와 유사한 알고리즘을 갖는다고 생각하였다.
#현재 피어있는 꽃 X의 종료 시점과 X의 종료시점 이전부터 피어있는 꽃들 중 종료 시점이 가장 늦은 꽃 Y를 찾는 방식이다.
#X의 종료시점과 Y의 시작시점만 알 수 있다면 여러가지 조건을 통해 해결할 수 있다.
#따라서 피는 날짜가 X의 종료시점과 겹쳐있고, 지는 날짜가 가장 늦은 Y를 반복을 통해 찾는 알고리즘을 선택하였다.
#11/30일까지만 꽃이 피어있으면 되기에 임의의 꽃의 지는 달이 12월을 넘지만 않으면 된다.
#이 때 주의할 점으로, 예를 들어 5/5보다 나중의 날짜를 찾기 위해서 조건문 중 and연산을 포함시키면 안된다. (if '비교할 달'>5월 and '비교할 일'>5일)
#그 이유는 만약 month가 더 커도,(ex 6월) day가 더 작으면 조건문에서 false가 성립되기 때문이다.(4일)
#결론적으로 5월 5일과 6월 4일을 비교하는데, and연산을 통해서는 6월 4일의 날짜가 5월 5일보다 큰, 즉 나중 날짜라고 판별되지 않는다는 것이다.
#따라서 아래의 코드처럼, 먼저 month를 비교하고 원하는 연산이 되었다면 그 하위 조건문으로 day를 비교하는 계단식 조건 방식을 사용해야 판별이 가능하다.

##시간복잡도##
#우선 while반복문을 통해, month가 12월을 넘기 전까지 반복을 진행한다. 이 횟수를 k라고 하자.
#while 내부의 for반복문에서는, 항상 n회, 즉 꽃의 종류 갯수 만큼 반복을 진행한다.
#이는 즉 k*n회의 반복이 진행되는 것인데, k의 크기에 따라 효율이 크게 달라질 수 있다.
#따라서 시간 복잡도 측면에서 아주 좋은 방식은 아니라고 본다.
#worst case : O(k*n) (n=꽃의 종류 갯수)

def princess_garden(n,flowers):
    answer = 0
    #현재 피어있는 꽃의 종료 날짜
    mon, day = 3, 1 #초기값은 항상 피어있어야 할 날짜의 시작점인 3월 1일로 설정
    tmp = 0
    while mon<12: #11월 30일까지만 꽃이 정원에 있으면 됨.
        fin_mon, fin_day = 0, 0 # 바뀔 꽃의 종료 날짜
        #현재 피어있는 꽃의 종료 이전에 피어 있으면서, 가장 종료 시점이 늦은(큰)꽃 탐색
        for k in range(len(flowers)):
            #항상 정원에 꽃이 있기 위해서는 현재 정원에 있는 꽃이 지기 전에 피어있는 꽃이 있어야 함.
            #다음에 올 꽃은 항상 이전 꽃의 종료 달과 일 이전에 피어있어야 함. and연산을 사용하면 안됨!
            if flowers[k][0] <= mon:
                if flowers[k][1] <= day:
                    # 현재 피어있는 꽃의 종료 이전에 피어있는 꽃의 종료 시점 비교(더 나중에 종료되는 꽃 찾기)
                    if flowers[k][2] > fin_mon: #month가 더 크면 항상 종료 시점이 더 늦음.
                        fin_mon, fin_day = flowers[k][2], flowers[k][3]
                    elif flowers[k][2] == fin_mon: #month가 같다면 day가 더 큰 꽃 선택.
                        if flowers[k][3] > fin_day:
                            fin_mon, fin_day = flowers[k][2], flowers[k][3]
                        tmp = k

        # 현재 피어있는 꽃의 종료 시점을 최신화
        mon, day = fin_mon, fin_day
        print(mon,day)
        answer += 1
        flowers = flowers[tmp+1:]
    return answer
'''
n = int(input())
flowers = []
for i in range(n): 
    flowers.append([int(x) for x in input().split()])
print(flowers)
'''
n = 4
flowers = [[1,1,5,31],[1,1,6,30],[5,15,8,31],[6,10,12,10]]
print(princess_garden(n,flowers))







