###Greedy_조이스틱 조작하여 이름 설정하기(2)###

## my algorithm ##
#이 문제의 핵심은 '▲(up)'과 '▼(down)'의 횟수 줄이기도 중요하지만, 사이드 조작(left, right)이 핵심이라고 생각하였다.
#만약 "JAX"라는 이름은 두번째 요소인 A로 넘어가는거보다, left기능을 수행하여 마지막 문자로 도달하는것이 더 좋은 greedy한 선택이다.
#이처럼 문자열 중 A를 만나면, A는 up or down을 수행하지 않아도 되기에 건너뛸 수 있다면 건너뛰는것이 조작 횟수를 최소화 시켜줄 수 있을것이다.
#따라서 문자 A를 만났을 때, 당장의 탐욕적 선택으로 right으로 마지막 문자에 도달할지 혹은 돌아가서 left기능을 수행할지에 대해 고민해야한다.
#이 때, right으로만 마지막 문자까지 도달하는 것은 총 문자열 길이-1, 즉 index마지막 수 만큼 진행된다,
#그리고 A를 만나 left를 수행하게 되는 경우는, 꼭 모든 side조작이 left가 아니라 하더라도,(right수행 도중 A를 만나 left로 선회할 수도 있다!)
#right으로만 수행하는 횟수에서 -1을 해주면 된다. 그 이유는 해당 문자 A를 무시하고 side조작을 하기 때문에 처음 만난 A의 side조작 한 회가 차감되는 것이다.
#이 때 혹시 처음 만나는 A 이후에 또 A가 있으면 다시 탐욕적 선택을 진행해야하냐고 의문을 가질 수도 있다.
#나는 이름 문자열 진행 중 처음 만나는 A에 대해서만 판단하면 된다고 생각을 하였는데,
#그 이유는 처음 만난 A에 대하여 left수행을 할 필요가 없는 문자열일 경우에는 당연히 그 이후 A들도 마찬가지 원리일 것이라고 생각하였다.(이후 나오는 A에서 left를 하면 횟수가 기존 문자열 길이보다 초과할지도??)
#처음에는 반복문을 진행하며 각 round마다 right와 left변수에 대해 판단하며 +1씩 하며 진행하려 했다.
#하지만 이는 너무 복잡해지고, right만 사용했을 때의 side조작횟수(문자열길이-1)와 left를 사용하게 됐을 경우의 side조작횟수(문자열길이-2)를 정규화 할 수 있음을 찾아냈기 때문에
#right와 left변수를 따로 선언하지 않고 side변수 하나로, A를 만났을 때의 greedy 방식을 조건문으로 적용하여 side변수에 값을 주는 방식을 선택하였다.
#up과 down은, 해당 문자열이 알파벳 전체의 절반(A~M, N~Z)중 어느 부분에 해당하는지 판단한 후에(배열 사용) 더 조작횟수가 적어지는 방식으로 진행한다.

##시간복잡도##
#문자열 전체를 돌며 up과 down의 횟수를 판별해야 하기 때문에 문자열 길이 n만큼 round를 반복한다.
#나머지 up과 down에 대한 삽입 연산과 A를 만났을 때의 조건, 비교, 삽입 연산은 상수 시간 C만큼이 소요되기때문에 큰 영향을 미치지 않는다.
#worst case : O(n) (n=문자열 길이)

def solution(name):
    answer = 0
    side, up, down = 0,0,0 #알고리즘 방식에서 설명한 대로 right와 left는 side변수로 통합하였다.
    alp_front = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']#알파벳 전반부
    alp_back = ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N']#알파벳 후반부
    for i in range(len(name)):
        if name[i] in alp_front:
            up += alp_front.index(name[i])
        elif name[i] in alp_back:
            down += alp_back.index(name[i]) + 1
        # front리스트의 알파벳은 A부터 출발하기 때문에 B로 넘어가는 순간에 up이 추가된다. 따라서 인덱스 번호 자체가 움직인 횟수가 된다.
        # 하지만 back리스트는 Z,즉 리스트의 첫 요소부터가 A로부터 down이 1회 된 것이기 때문에 Z로 이동한 횟수인 +1을 해주어야한다.
    if "A" in name:
         if len(name)-name.index("A") < (name.index("A")-1) + ((len(name)-1) - name.index("A")):
             #A부터 마지막까지 right을 수행했을 때의 조작 횟수 vs A로 가지 않고 left를 수행하여서 마지막 문자까지 도달하는 조작 횟수
             side = len(name)-1
             # A부터 마지막까지 right을 수행했을 때의 조작 횟수가 적으면 right조작을 쭉 진행. 이는 문자열 길이-1 만큼 조작한다!
         else :
             side = len(name)-2
             # A로 가지 않고 left를 수행하여서 마지막 문자까지 도달하는 조작 횟수가 적으면 left조작 진행.이는 문자열 길이-2 만큼 조작한다!
    else : side = len(name)-1
    #A를 만나지 않으면 그냥 쭉 편하게 right으로 넘어가면 됩니다 ㅎㅎ

    answer = side + up + down
    #모든 최소 조작 횟수의 합..

    return answer

'''
name = "JEROEN"
name2 = "JAN"
print(solution(name))
print(solution(name2))
'''

###result###
#81.8 / 100.0