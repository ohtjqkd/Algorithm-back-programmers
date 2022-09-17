import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;
import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

class Solution {
    public int[] solution(int[] fees, String[] records) {

        int carCnt = 0;
        HashMap<String, Queue<String>> map = new HashMap<>();
        for (String r : records) {
            String[] spl = r.split(" ");
            Queue<String> get = map.get(spl[1]);
            if (get != null) {
                get.add(spl[0]);
            } else {
                Queue<String> q = new LinkedList<String>();
                q.add(spl[0]);
                map.put(spl[1], q);
            }
        }
        
        List<String> cars = new ArrayList<String>(map.keySet());
        
        Collections.sort(cars);
        int[] answer = new int[cars.size()];
        int idx = 0;
        for (String c : cars) {
            Queue<String> get = map.get(c);
            int totalTime = 0;
            while (get.peek() != null) {
                String inTime = get.poll();
                String outTime;
                if (get.peek() == null) outTime = "23:59";
                else outTime = get.poll();
                totalTime += getTime(outTime) - getTime(inTime);
            }
            answer[idx++] = getFee(fees, totalTime);
        }
        return answer;
    }
    
    private int getTime(String t) {
        String[] spl = t.split(":");
        return Integer.parseInt(spl[0]) * 60 + Integer.parseInt(spl[1]);
    }
    
    private int getFee(int[] fee, int totalTime) {
        System.out.println(totalTime);
        if (totalTime <= fee[0]) return fee[1];
        double dFee = (totalTime - fee[0]) / (double) fee[2];
        return (int) (Math.ceil(dFee)) * fee[3] + fee[1];
    }
}