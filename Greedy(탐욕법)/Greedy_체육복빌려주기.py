###Greedy_체육복빌려주기###

## my algorithm ##
#수업 참여 가능한 maximum 학생 수 = 전체학생수 n - 체육복 없는 학생 수
#따라서 answer값을 구하기 위해 체육복 빌리기에 성공한 학생 수를 책정하는 변수 key를 설정하였다.
#자신의 -1 or +1인 학생의 체육복만 빌릴 수 있으므로, lost학생 수 만큼 반복을 돌며 lost 각자의 -1 혹은 +1인 학생이 여분이 있는지 탐색한다.
#만약 알맞는 reserve학생을 찾았으면, 그 인덱스는 reserve에서 지우고 key값을 -1 해준다. 한 학생 당 최대 하나의 여분만 있을 수 있기 때문이다.
#만약 여분을 갖고있는 학생 배열 reserve의 요소가 사라지면 반복을 중단한다.
#최종적으로 결정된 key값(기존 lost학생수 -= 체육복 빌리기에 성공한 학생)을 전체 학생수 n에서 빼주면 answer가 된다.

##시간복잡도##
#최대 lost의 길이만큼 반복한다. lost의 길이는 최대 학생 수 n을 넘을 수 없기 때문에 최대 O(n)이 된다.
#worst case : O(n) (n=학생 수)



def solution(n, lost, reserve):
    answer = 0
    key = len(lost)#key = 체육복 lost 상태인 학생 수 최신화를 위한 변수
    for i in lost: #lost의 요소 i에 대하여
        if reserve == None:break #reserve가 None -> lost를 해결할 수 없으므로 break.
        if i-1 in reserve: #자신의 앞 순서 is in reserve(대여 가능)
            reserve.remove(i-1)
            key-=1 #해당 학생을 대여가능에서 없애고, lost학생 수 한 명 감소.
        elif i+1 in reserve: #자신의 뒷 순서 is in reserve(대여 가능)
            reserve.remove(i+1)
            key-=1 #해당 학생을 대여가능에서 없애고, lost학생 수 한 명 감소.
    answer = n - key #전체 학생 수에서 최신화 된 lost학생 수 만큼을 뺀 것.
    return answer

n = 5
lost = [2,4]
reserve = [1,3,5]
print(solution(n,lost,reserve))

###result###
#75.0 / 100.0