import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer_arr = new ArrayList<>();
        ArrayList<Integer> arr = new ArrayList<>();
        
        for(int i=0; i<progresses.length; i++){
            int left_days = 100 - progresses[i];
            int due = (int)Math.ceil((double)left_days/speeds[i]);
            //System.out.println(due);
            arr.add(due);
        }
        
        int index = 1;
        int _max_ = arr.get(0); //첫번째 작업 속도를 max로 설정
        for(int j=0; j<arr.size(); j++){
            if(j == arr.size()-1){
                answer_arr.add(index);
            }
            else if(_max_ < arr.get(j+1)){ //max가 그 다음에 오는 수보다 작으면 바로 배포
                answer_arr.add(index);
                _max_ = arr.get(j+1); 
                index = 1;
            }
            else if(_max_ >= arr.get(j+1)){
                index += 1;
            }
        }
        
        int[] answer = new int[answer_arr.size()];
        for(int k=0; k<answer_arr.size(); k++){
            answer[k] = answer_arr.get(k);
        }
        return answer;
    }
}