import java.util.*;

// 각 의상종류마다의 의상 개수를 파악하고, 이를 활용하여 해결할 수 있는 문제
// 처음에는 '조합'을 이용해서 [ 전체 의상 조합 경우의 수 - 겹치는 의상 종류를 뺀 경우의 수 ] 로 해결하려 했음
// 그런데 생각해보니, 의상종류 A가 가능한 다른 의상종류들의 경우를 모두  구한 후 더하면 의상종류가 겹치지 않는 모든 경우의 수 구할 수 있음
//예를 들어 ["headgear" : 2] (headgear종류 의상 2개 // 어떤 의상인지는 상세 이름은 크게 상관 없음) , ["eyewear" : 1] (eyewear종류 의상 1개)라면, 각각 입지 않는 경우를 포함하여  heargear는 2+1의 3가지 경우, eyewear는 1+1의 2가지 경우이다.
// 따라서 headgear 하나당 가능한 eyewear의 경우는 2가지씩이므로 
// 2(headgear 하나당 가능한 eyewear) * 3(headgear의 경우의 수) = 6 인데,
// 스파이는 최소 하나 이상의 의상을 입어야 하므로 두 경우 모두 안입는 경우를 하나 빼줘야 한다.
// 이 알고리즘을 해결하기 위해, 각 의상종류마다 의상의 수를 저장할 자료구조 필요하다.
// ==>Map을 사용해서 { 의상종류 : 의상 갯수 } 와 같이 저장한다.
// 또한 Map의 key는 중복되면 안되고, 중복된 key가 다시 입력될 경우 value가 update되기에
// Java영역에서 제공하는 .getOrDefault() 를 사용하여 삽입하려는 자료의 key가 이미 있다면 해당 key로 된 자료의 value에 추가 조치를 해주었다.
// 또한 최종 결과값을 구할 때는 Java Map 함수인 .entrySet() 을 사용하여 Map에 담긴 자료들의 key와 value 쌍을 하나씩 확인할 수 있도록 하였다. 이를 통해 각 value에 접근해 answer 도출!

// *getOrDefault() 함수 말고 .containsKey(key) 함수로 해당 key의 유무를 파악 가능!

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String, Integer> hm = new HashMap<>();
        //clothes 2차원 배열 각 요소의 1번째 index(의상 종류)를 key로 하는 map 생성
        for(int i=0; i<clothes.length; i++){ 
            hm.put(clothes[i][1], hm.getOrDefault(clothes[i][1], 1)+1);
        }
        int size = hm.size();
        //map에 담긴 key들의 value(옷 종류의 수) 모두 곱하여 경우의 수 생산
        for(Map.Entry<String, Integer> entry : hm.entrySet()){
            answer *= entry.getValue();
        }
        answer -= 1; //최소 하나의 의상은 입어야하므로 모두 안입은 경우 하나 제외
        return answer;
    }
}