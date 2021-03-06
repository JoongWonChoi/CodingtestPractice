###Greedy_큰 수의 법칙(이것이 코딩테스트다)###

## my algorithm ##
#num배열의 수들을 대상으로, 총 m회 더하여 가장 큰 수를 만들어야 한다.
#이 때, 한 수에 대하여 k회 반복을 초과하면 안된다.
#k회 반복을 한 후, 그 다음으로 큰 수를 더하고, 다시 가장 큰 수를 더할 수 있다.
#보통은 while 혹은 for 반복문을 통해 수를 차례로 더할 생각을 할 것이다.
#하지만 이 문제를 파헤쳐보면, 배열 num에서 가장 큰 수 2개만 있으면 됨을 알 것이다. 어차피 가장 큰수 a를 k회 반복하여 더하고, 그 다음으로 큰 수인 b를 더해주며 휴게소에 들린 것 같은 효과를 줄 수 있기 때문이다.
#보통 큰 수를 반복문을 통해 차례로 더한다 하면, sort를 하여 차례로 수를 정렬해야 할 것이다.
#시간 복잡도를 따져보면 배열 num의 길이 n을 기준으로 nlogn의 시간이 들지만, 나의 알고리즘에 의하면 가장 큰 수 2개만 찾으면 되기에 max함수를 두번만 사용하면 된다.
#이는 길이 n에 대한 max함수에 소요되는 시간, 즉 n만큼의 시간이 걸리고, 두 수를 구해야하므로 n*2만큼의 시간이 소요된다.
#단순하게 생각해보면, n*logn 과  n*2 는, n이 4이상이 되는 순간 절대적으로 2*n이 적은 시간이 드는 것을 알 수 있다.
#또한 규칙을 찾아보면 반복을 하지 않고 문제를 해결할 수 있다.
#총 더해야하는 횟수 m회를, 연속으로 더해지는 횟수 k로 나눈 나머지가 key라고 하면, 두번째 큰 수 b를 key만큼 더하고, m-key만큼 모두 가장 큰 수 a를 더하면 된다.
#이는 반복을 이용하지 않고 문제 해결이 가능하여 시간을 효율적으로 관리할 수 있다.

##시간복잡도##
#num배열의 길이 n에 대하여 가장 큰 수와 그 다음 수를 찾는 과정이 필요하므로(max함수) --> 2*n 만큼 소요.
#나머지 과정은 단순한 연산과정들이므로 상수회 C 소요.
#따라서 O(2n), 즉 O(n)만큼의 시간 소요.
#worst case : O(n) (n=num배열의 길이)

def bigNum(n,m,k,num):
    answer = 0
    a = max(num)
    num.remove(a)
    b = max(num)
    key = m%k
    answer += a * (m-key)
    answer += b * key
    return answer

#다음은 정렬을 시행한 후 보통의 방식대로, 가장 큰 수부터 차례로 반복을 통해 더하며 해결해 가는 과정이다.
#이에 대한 시간복잡도는, 우선 정렬에 대한 nlogn 시간 // 반복에서의 시간은, M의 크기에 비례하여 효울적이지 못하게 커질 수 있다.

def bigNum2(n,m,k,num):
    answer = 0
    num.sort(reverse = True) #num배열 내림차순 정렬
    while True:
        for i in range(k): #한 수에 대해 k회까지 반복 제어
            if m==0:break #총 더하는 횟수(m)가 끝나면 반복 종료
            answer += num[0] #m이 0이 아니라면 가장 큰수 k회만큼 덧셈 반복
            m-=1 #더해지는 횟수 1 차감
        if m==0:break #k회 반복 후 총 더하는 남여 횟수가 없으면 반복 종료
        answer += num[1] #그렇지 않으면 두번쨰로 큰 수 한번 더하기(휴게소)
        m-=1 #더해지는 횟수 1 차감 후 반복
    return answer

n, m, k = [int(x) for x in input().split()]
num = list(map(int, input().split()))
print(bigNum(n,m,k,num))