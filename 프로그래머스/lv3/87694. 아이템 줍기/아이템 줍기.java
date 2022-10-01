class Solution {
    int[] dx = {0, 1, 0, -1};
    int[] dy = {1, 0, -1, 0};
    int[][] map = new int[120][120];
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        int maxX = 0; int maxY = 0;
        for (int i = 0; i < rectangle.length; i++) {
            maxX = Math.max(rectangle[i][1], maxX);
            maxY = Math.max(rectangle[i][3], maxY);
            for (int j = 0; j < rectangle[i].length; j++) {
                rectangle[i][j] *= 2;
            }
        }
        maxX = (maxX + 10) * 2;
        maxY = (maxY + 10) * 2;

        for (int[] row: rectangle) {
            int x1 = row[0];
            int y1 = row[1];
            int x2 = row[2];
            int y2 = row[3];
            for (int i = x1; i < x2 + 1; i++) {
                for (int j = y1; j < y2 + 1; j++) {
                    if (this.map[i][j] != 2) {
                        if (i == x1 || i == x2 || j == y1 || j == y2) {
                            this.map[i][j] = 1;
                        } else {
                            this.map[i][j] = 2;
                        }
                    }
                }
            }
        }
        this.map[itemX * 2][itemY * 2] = 3;
        return dfs(new int[]{characterX * 2, characterY * 2}, 0, -1) / 2;
    }
    public int dfs(int[] nowLoc, int distance, int prevDir) {
        if (this.map[nowLoc[0]][nowLoc[1]] == 3) return distance;
        int x = nowLoc[0]; int y = nowLoc[1];
        int result = Integer.MAX_VALUE;
        for (int i = 0; i < 4; i++) {
            int xx = x + dx[i]; int yy = y + dy[i];
            if ((this.map[xx][yy] == 1 || this.map[xx][yy] == 3) && (i + 2) % 4 != prevDir) {
                int[] nextLoc = {xx, yy};
                result = Math.min(dfs(nextLoc, distance + 1, i), result);
            }
        }
        return result;
    }
}