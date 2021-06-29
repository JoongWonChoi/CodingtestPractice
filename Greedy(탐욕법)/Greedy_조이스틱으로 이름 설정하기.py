###Greedy_조이스틱 조작하여 이름 설정하기###



def solution(name):
    answer = 0
    left,right,up,down = 0,0,0,0
    alp_front = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    alp_back = ['Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N']
    i = 0
    ##'▶'(right) 동작을 수행하는 반복문
    while i<len(name):
        if name[i] == 'A':
            if len(name) - 1 <= (i * 2) + ((len(name) - 1) - (i + 1) + 1):
            #'▶'(right)만을 수행하여 이름의 마지막 알파벳까지 도달하는것이 A를 만나 '◀'(left)을 사용하여 왼쪽 알파벳들을 탐색하는 방법보다 짧다면 그냥 오른쪽으로 쭉 이동하며 진행한다.
                if i > 0: right += 1
                #이름의 두번째 알파벳으로 넘어가면서부터 '▶'(right)을 동작한다.
            else:
                break
            #A를 만나 좌측으로 돌아가는게 조작 횟수가 더 적다면 right동작을 수행하는 현재의 반복문을 종료하고, left동작을 수행하는 반복문으로 넘어간다.
            #이 때의 i는 A가 위치한 인덱스 번호이다.
        if name[i] in alp_front:
            up += alp_front.index(name[i])
        elif name[i] in alp_back:
            down += alp_back.index(name[i]) + 1
        i +=1
        # front리스트의 알파벳은 A부터 출발하기 때문에 B로 넘어가는 순간에 up이 추가된다. 따라서 인덱스 번호 자체가 움직인 횟수가 된다.
        # 하지만 back리스트는 Z,즉 리스트의 첫 요소부터가 A로부터 down이 1회 된 것이기 때문에 Z로 이동한 횟수인 +1을 해주어야한다.
    left += (i-1)
   ##'◀'(left) 동작을 수행하는 반복문
    while True:
        left += 1
        #A를 만나 A가 위치한 인덱스의 previous index로 넘어가기 위해 '◀'(left)를 동작한다.

    answer = left + right + up + down

    return answer







'''
    for i in range(len(name)):
        if i=='A':
            if len(name)-1 >= (i*2) + ((len(name)-1)-(i+1)+1):
                if i>0 : right += 1
            else : left += 1
        if name[i] in alp_front:
            up += alp_front.index(name[i])
        elif name[i] in alp_back:
            down += alp_back.index(name[i])+1
        #front리스트의 알파벳은 A부터 출발하기 때문에 B로 넘어가는 순간에 up이 추가된다. 따라서 인덱스 번호 자체가 움직인 횟수가 된다.
        #하지만 back리스트는 Z,즉 리스트의 첫 요소부터가 A로부터 down이 1회 된 것이기 때문에 Z로 이동한 횟수인 +1을 해주어야한다.
'''




name = "JEROEN"
name2 = "JAN"
print(solution(name))
print(solution(name2))