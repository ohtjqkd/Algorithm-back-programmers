import java.util.HashSet;

class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int[][] answer = new int[m][n];
        answer[0][0] = 1;
        HashSet<Integer> set = new HashSet<>();
        for (int[] p : puddles) {
            set.add(n * (p[0] - 1) + p[1] - 1);
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (set.contains(i * n + j) || (i + j) == 0) continue;
                answer[i][j] = (answer[Math.max(0, i - 1)][j] + answer[i][Math.max(0, j - 1)]) % 1000000007;
            }
        }
        
        
        return answer[m - 1][n - 1];
    }
    
    public String stringLoc(int i, int j) {
        StringBuffer result = new StringBuffer();
        result.append(String.valueOf(i));
        result.append(",");
        result.append(String.valueOf(j));
        return result.toString();
        // return String.valueOf(i)+","+String.valueOf(j);
    }
}