###Greedy_구명보트###

## my algorithm ##
#정해져있는 보트의 무게 limit, 최대 2명까지 태울수 있는 보트에 최소한의 횟수로 사람을 태워 구조해야한다.
#이 문제의 key는 최대 두명까지 태울 수 있는 보트와 보트에 태울 수 있는 limit 이다.
#구조해야할 사람의 무게가 배열로 [50,70,50,80] 이고 보트의 limit이 100 이라면, 첫번째 사람과 세번째 사람을 같이 태우는 것 외에는 모두 한명씩 태워야한다.
#따라서 최소 운송 횟수는 3회가 된다.
#앞선 알고리즘은 사람의 배열을 전부 다 탐색하는 방법을 사용하였다. 이는 n회 반복이지만, 사람의 수가 많아지면 그 수만큼 비례하여 증가한다는 의미이다.
#이의 한계점을 보완하기 위해 배열을 전부 다 탐색하지 않고, 특정 경우가 되면 나머지 요소들을 처리할 수 있는 알고리즘을 생각해보았다.
#이에 내가 생각한 알고리즘은, 배열을 내림차순으로 정렬 후 limit과 비교를 하며, limit의 무게의 절반인 사람이 나타날 때 까지 반복을 하는 방법이다.
#예를 들어 구조해야할 사람잉 100명이면, 몸무게를 내림차순으로 정렬 후, 첫번째 무게의 사람과 마지막 무게(제일 가벼움)의 사람이 함께 보트에 탑승 가능한지 판단한다.
#그 이유는, 가장 무거운 사람은 가장 가벼운 사람과 동승이 안되면 항상 누구와도 동승이 안되기 때문이다.
#이런식으로 경우를 따지며 동행이 가능하면 두번째로 무거운 사람과 두번째로 가벼운 사람을 비교하고, else이면 두번째로 무거운 사람과 가장 가벼운 사람은 그대로 비교 대상으로 설정한다.
#진행을 하다보면, 가장 무거운 사람의 무게가 limit의 절반 이하가 되는 경우가 올 수 있다.
#그렇다면 그 이후의 사람은 모두 더욱 가벼운 사람들이므로, 항상 아무 누구와 짝을 이루어도 limit보다 작거나 같을 것이다.
#이를 이용해, 남은 인원이 짝수일때는 인원의 절반 만큼을, 홀수 일때는 절반+1(두명씩 짝지어도 한 명이 남기 떄문) 만큼의 보트가 필요하다.
#따라서 남은 배열 요소들은 반복문을 통해 탐색하지 않아도 이러한 조건식을 통해 반복을 더이상 진행하지 않아도 되기에 수행시간이 확연히 줄어든다.
#이번 문제를 통해 느낀점은, 항상 n에 대하여 가장 큰 차수를 가진 연산과정만이 시간복잡도 Big O에 영향을 주고, 그 이하의 연산과정에서 소요되는 시간은 크게 영향을 미치지 않는다고 생각하였다.
#하지만 이번 해결 과정과 같이, 시간 복잡도는 저번 알고리즘과 같이 sort()함수 만큼의 시간이 소요되겠지만, 1차원 반복문에 대한 연산 과정을 줄일 수 있다면 더욱 효율적인 수행이 가능하다.
#따라서 언제나 반복에 대해서는 문제 해결 과정에서 꼭 반복문을 다 돌지 않고도 문제를 해결 가능한 방법이 있는지 생각해보고 알고리즘을 짜야함을 아~~~주 크게 느꼈다.

##시간복잡도##
#최대 people의 길이만큼 반복한다. people 배열 내에서 두명 을 태우면 그만큼 해당 요소가 skip되므로 최대 배열 길이 이하로 반복한다.
#그 전에 people배열을 sort하는 과정에서 nlogn의 시간이 소요된다.
#worst case : O(nlogn) (n=사람 수)

def solution(people, limit):
    answer = 0
    left, right = 0, len(people) - 1 #가장 무거운사람 : left, 가장 가벼운사람 : right. 배열 탐색을 위한 변수. 각 round마다 배열의 처음과 끝을 pointing한다고 보면 됨!
    count = len(people) # left<=limit이 되면 남은 사람에 대하여 보트 수를 정해야하는데, 이 때 연산을 용이하게 해줄 용도. 구조되는 사람 수 만큼 차감되는 변수이다.
    people.sort(reverse=True) #내림차순 정렬. 가장 무거운 사람이 가장 처음 인덱스로!!
    while True:
        if left==right: #사람이 한명 남는 경우!
            answer+=1 #보트 한개 무조건 필요
            break
        if people[left] <= limit//2: #가장 무거운 사람의 무게 <= 제한무게  ... 남은 인원들은 무조건 두명씩 동승 가능!
            if count%2==0: # 남은 인원이 짝수 : 보트 인원수 // 2 개만 필요
                answer += count//2
            else: # 남은 인원이 홀수 : 보트 인원수 // 2 + 1개 필요(2명씩 매칭 후 마지막에 한명이 남기 때문)
                answer += (count//2) + 1
            break
        if people[left] + people[right] <= limit: #가장 무거운 사람 + 가장 가벼운 사람의 무게가 limit보다 작으면 같이 태워 횟수를 줄인다.
            answer+=1
            left+=1 #다음으로 무게가 많은 사람으로 point 이동
            right-=1 #다음으로 가벼운 사람으로 point 이동
            count-=2
        else: #그렇지 않다면 가장 무게가 나가는 사람 한명밖에 보트에 못태운다.
            answer+=1
            left+=1 #다음으로 무게가 많은 사람으로 point 이동
            count-=1

    return answer