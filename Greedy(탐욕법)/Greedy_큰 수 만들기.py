###Greedy_큰 수 만들기###

## my algorithm ##
#순서가 있는 수 문자열 중에서 k개 만큼의 수를 제거한 후 만들 수 있는 가장 큰 수를 return 해야한다.
#이 때 수 문자열 내의 숫자 선후 관계는 변하면 안된다.
#나는 수 문자열 첫번째 요소부터 탐색하며 가장 큰 수가 return될 수 있도록 앞에서부터 순차적으로 제거하면서, k개만큼 제거하면 반복을 종료하는 알고리즘을 생각했다.
#Test case 문제들은 만족을 했지만 효율성 및 완성도가 매우 부족한 결과가 나왔다.
#다시 해결 과정을 생각해보아야할 것 같다 . . .

##시간복잡도##
#count변수를 설정하고, 숫자를 제거하는 과정을 k회 반복한다. --> 최대 배열 길이 n
#여기에 반복을 하는 과정에서 배열에 대한 min함수를 사용하므로 최대 배열의 길이 n만큼 곱해진다.
#worst case : O(n^2) (n=수 문자열의 길이)



def solution(number, k):
    answer = ''
    i = 1
    cnt = 0
    left = 0
    while cnt < k:
        if i == len(number)-1: left+=1
        if left >= len(number):
            break
        if number[left] < number[i]:
            tmp = min(number[:i + 1])
            idx = number.index(tmp)
            number = number[:idx] + number[idx + 1:]
            cnt += 1
            i = 1
            left = 0
        else:
            i += 1
    answer = number

    return answer


number = "4177252841"
k = 4
print(solution(number,k))