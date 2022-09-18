class Solution {
    public int[] solution(long n) {
        int len = 1;
        if (n % 10 == 0) len--;
        int[] answer = new int[(int) Math.log10(n) + 1];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = (int) (n % 10);
            n /= 10;
        }
        return answer;
    }
}