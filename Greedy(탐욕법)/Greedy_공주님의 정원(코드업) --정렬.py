###Greedy_공주님의 정원(코드업) --두번째 시도###

## my algorithm ##
#3/1부터 11/30까지 공주님의 정원에 항상 꽃이 적어도 하나 이상 피어있도록 설계해야한다.
#이 문제는 잘 알려져있는 강의실 배정 문제와 유사한 알고리즘을 갖는다고 생각하였다.
#이전의 방식과는 다르게 꽃 리스트를 끝나는 month 기준으로 오름차순 정렬을 먼저 시행하였다.
#그렇게 하면 이중반복을 사용하지 않고, 리스트 인덱스를 순차적으로 포인팅 해가며 진행할 수 있다.
#현재 피어있는 꽃X의 종료일을 기준으로 삼는 변수를 생성하고, 리스트를 순회하며 X의 종료일 이전에 피는 꽃 Y에 대하여 종료시점이 가장 늦는 Y를 구한다.
#그러면 현재 피어있는 꽃이 Y가 되고, 같은 방식으로 반복을 진행한다.
#마찬가지로 현재 피어있는 꽃의 month가 12를 넘어가면 반복을 중단한다.

##시간복잡도##
#리스트 정렬을 nlogn 시간에 걸쳐 진행
#그 후 리스트를 하나씩 순회하며 진행
#이중반복을 사용하지 않고 정렬 1회와 1차원 반복을 별개로 진행하였는데 왜 시간 초과가 발생하는지 모르겠다. 다른 방법을 찾아봐야 할 것 같다.


def princess_garden(n,flowers):
    answer = 1
    flowers.sort(key=lambda x:x[2]) #각 꽃의 종료 month기준으로 정렬
    #현재 피어있는 꽃의 종료 날짜
    mon, day = 3, 1 #초기값은 항상 피어있어야 할 날짜의 시작점인 3월 1일로 설정
    fin_mon, fin_day = 0, 0
    idx = 0
    while mon<12:
        if idx>=n: break #바닥조건
        # 현재 꽃 종료일보다 다음 꽃 시작일이 큰 경우 => 꽃 종류 달라지고, 현재 꽃 최신화(종료 시점)
        if flowers[idx][0] > mon:
            answer += 1 #꽃이 교체될 때 정답+1
            mon, day = fin_mon, fin_day
            fin_mon, fin_day = 0, 0

        # 현재 꽃의 종료 날짜 이전에 피어있는 꽃 탐색. 그래야 정원에 항상 꽃이 존재함.
        elif flowers[idx][0] < mon:
            if flowers[idx][2] > fin_mon:
                fin_mon, fin_day = flowers[idx][2], flowers[idx][3]
            elif flowers[idx][2] == fin_mon:
                if flowers[idx][3] > fin_day:
                    fin_mon, fin_day = flowers[idx][2], flowers[idx][3]
            idx += 1
        elif flowers[idx][0]==mon:
            if flowers[idx][1] < day:
                if flowers[idx][2] > fin_mon:
                    fin_mon, fin_day = flowers[idx][2], flowers[idx][3]
                elif flowers[idx][2] == fin_mon:
                    if flowers[idx][3] > fin_day:
                        fin_mon, fin_day = flowers[idx][2], flowers[idx][3]
                idx += 1
    return answer

n = int(input())
flowers = []
for i in range(n):
    flowers.append([int(x) for x in input().split()])

print(princess_garden(n,flowers))





