class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        String ret;
        ret = convertK(n, k);
        String[] split = ret.split("0");
        for (String s : split) {
            // System.out.println(s);
            if (s.equals("")) continue;
            if (isPrime(Long.parseLong(s))) answer++;
        }
        return answer;
    }
    
    private String convertK(int n, int k) {
        String ret = "";
        while (n > 0) {
            ret = String.valueOf(n % k) + ret;
            n = n / k;
        }
        return ret;
    }
    
    private boolean isPrime(Long n) {
        if (n == 1) return false;
        if (n == 2) return true;
        for (Long i = 2l; i < Math.sqrt(n) + 1; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}