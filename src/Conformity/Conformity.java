import java.io.*;
import java.util.*;

public class Conformity {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);

        Map<Integer,Integer> hm = new HashMap<Integer,Integer>();
        int maxPop = 0;
        int ans = 0;
        
        int n = Integer.parseInt(sc.readLine());
        for (int i = 0; i < n; i++) {
            String[] line = sc.readLine().split(" ");
            int combination = 1;
            for (int j = 0; j < 5; j++) {
                combination *= (901-Integer.parseInt(line[j])); // random thought and number
            }
            if (hm.containsKey(combination)) {
                hm.put(combination,hm.get(combination)+1);
                maxPop = Math.max(hm.get(combination),maxPop);
            } else {
                hm.put(combination,1);
                if (maxPop == 0) {
                    maxPop++;
                }
            }
        }

        for (Integer c : hm.keySet()) {
            if (hm.get(c) == maxPop) {
                ans += maxPop;
            }
        }
        
        writer.print(ans);
        writer.flush();
    }
}