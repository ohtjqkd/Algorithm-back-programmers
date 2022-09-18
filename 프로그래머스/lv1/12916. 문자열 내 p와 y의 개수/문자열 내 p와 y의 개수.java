class Solution {
    boolean solution(String s) {
        boolean answer = true;
        int pCnt = 0;
        int yCnt = 0;
        String[] tmp = s.split("");
        for(int i = 0;i<s.length(); i++){
            if(tmp[i].equalsIgnoreCase("p")) pCnt++;
            if(tmp[i].equalsIgnoreCase("y")) yCnt++;
        }
        answer = pCnt == yCnt;
        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("Hello Java");

        return answer;
    }
}