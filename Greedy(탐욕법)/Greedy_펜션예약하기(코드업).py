###Greedy_펜션예약하기(이것이 코딩테스트다)###

def reserve(n, k, res, s, t):
    answer = 0
    idx = s  # 여행 첫 날
    tmp = []  # 예약 가능한 방 리스트

    while idx < t:  # 여행 마지막날 전까지만 탐색
        if len(tmp) != 0:  # 만약 예약 가능한 방이 하나라도 있다면

            for i in range(len(tmp) - 1, -1, -1):  # pop함수 사용 위해 마지막 인덱스부터 확인
                if res[idx][tmp[i]] == 'X':  # 전에 예약 가능했던 방이 다음날 예약 불가능 하면
                    tmp.pop()  # 그 방은 리스트에서 제외.

        if len(tmp) == 0:  # 예약 가능한 방 x (tmp 공백)
            if idx > s:  # 탐색할 날짜가 여행 첫날이면 방 옮긴 횟수에 추가 안해도 됨.
                answer += 1
            for i in range(k):  # 펜션 방 탐색
                if res[idx - 1][i] == 'O':
                    tmp.append(i)

        idx += 1  # 다음날로 진행!

    return answer


n, k = [int(x) for x in input().split()]
res = []
for i in range(n):
    res.append(input())
s, t = [int(x) for x in input().split()]
print(reserve(n, k, res, s, t))