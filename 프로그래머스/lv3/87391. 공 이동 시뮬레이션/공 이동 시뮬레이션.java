import java.util.Stack;
import java.util.LinkedList;

class Solution {

    
    public long solution(int n, int m, int x, int y, int[][] queries) {
        long answer = 0;
        Stack[] stacks = new Stack[2];
        stacks[0] = new Stack<Integer>();
        stacks[1] = new Stack<Integer>();
        
        for (int[] q : queries) {
            int div = q[0] / 2;
            int mod = q[0] % 2;
            if (mod == 0) stacks[div].push(-q[1]);
            else stacks[div].push(q[1]);
        }
        return (long) (availRange(stacks[0], y, m)) * (long) (availRange(stacks[1], x, n));
    }
    
    private int availRange(Stack<Integer> q, int dest, int wall) {
        int mn = dest;
        int mx = dest;
        while (!q.isEmpty()) {
            int dd = q.pop();
            if (dd < 0) {
                if (mn > 0) mn = Math.max(0, mn - dd);
                else if (mx - dd < 0) return 0;
                mx = Math.min(mx - dd, wall - 1);
            } else {
                if (mx < wall - 1) mx = Math.min(mx - dd, wall - 1);
                else if (mn - dd > wall - 1) return 0;
                mn = Math.max(0, mn - dd);
            }
        }
        return mx - mn + 1;
    }
}