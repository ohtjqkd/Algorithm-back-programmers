import java.util.ArrayList;
import java.util.Arrays;
class Solution {
    int[][] bar;
    int[][] pillar;
    
    public int[][] solution(int n, int[][] build_frame) {
        ArrayList<int[]> answer = new ArrayList<int[]>();
        int[][] target;
        this.pillar = new int[n + 3][n + 3];
        this.bar = new int[n + 3][n + 3];
        int x, y, type, com;
        
        for (int[] b : build_frame) {
            x = b[0] + 1; y = b[1] + 1; type = b[2]; com = b[3];
            target = getTarget(type);
            if (com == 0) {
                target[x][y] = 0;
                if (!canDelete(x, y, type)) target[x][y] = 1;
            } else if (canStruct(x, y, type)) {
                target[x][y] = 1;
           }
        }
        for (int i = 1; i < n + 3; i++) {
            for (int j = 1; j < n + 3; j++) {
                if (this.pillar[i][j] == 1) {
                    int[] item = {i - 1, j - 1, 0};
                    answer.add(item);
                }
                if (this.bar[i][j] == 1) {
                    int[] item = {i - 1 , j - 1, 1};
                    answer.add(item);
                };
            }
        }
        
        // for (int[] a : this.pillar) {
        //     for (int b : a) {
        //         System.out.print(b);
        //     }
        //     System.out.println();
        // }
        // for (int[] a : this.bar) {
        //     for (int b : a) {
        //         System.out.print(b);
        //     }
        //     System.out.println();
        // }
        int[][] result = new int[answer.size()][3];
        int idx = 0;
        for (int[] a : answer) {
            result[idx++] = a;
        }
        return result;
    }
    
    public boolean checkPillar(int x, int y) {
        if (y == 1) return true;
        if (this.pillar[x][y - 1] == 1) return true;
        if (this.bar[x - 1][y] == 1 || this.bar[x][y] == 1) return true;
        return false;
    }
    
    public boolean checkBar(int x, int y) {
        if (this.pillar[x][y - 1] == 1 || this.pillar[x + 1][y - 1] == 1) return true;
        if (this.bar[x - 1][y] == 1 && this.bar[x + 1][y] == 1) return true;
        
        return false;
    }
    
    public boolean canDelete(int x, int y, int type) {
        int[][] target = getTarget(type);
        target[x][y] = 0;
        for (int i = x - 1; i < x + 2; i++) {
            for (int j = y; j < y + 2; j++) {
                if (this.pillar[i][j] == 1 && !checkPillar(i, j)) return false;
                else if (this.bar[i][j] == 1 && !checkBar(i, j)) return false;
            }
        }
        return true;
    }
    
    public boolean canStruct(int x, int y, int type) {
        if (type == 0) {
            return checkPillar(x, y);
        } else {
            return checkBar(x, y);
        }
    }
    
    public int[][] getTarget(int type) {
        if (type == 0) return this.pillar;
        else return this.bar;
    }
}