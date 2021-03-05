import java.io.*;
import java.util.*;

public class Conformity {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);

        Map<Long,Integer> hm = new HashMap<Long,Integer>();
        int maxPop = 0;
        int ans = 0;
        
        int n = Integer.parseInt(sc.readLine());
        for (int i = 0; i < n; i++) {
            String[] line = sc.readLine().split(" ");

            /*
            // A layman hashing function is to simply sort the list and use base to convert the list into integer/long
            List<Integer> temp = new ArrayList<Integer>();
            for (int j = 0; j < 5; j++) {
                temp.add(Integer.parseInt(line[j]));
            }
            Collections.sort(temp);
            
            // Use base 400 (any big number can do)
            long combination = 0L;
            for (int j = 0; j < 5; j++) {
                combination *= 400;
                combination += temp.get(j)-100;
            }
            */

            // This hashing function somehow works also in this case
            long combination = 1L;
            for (int j = 0; j < 5; j++) {
                combination *= (901-Integer.parseInt(line[j])); // random thought and number
            }
            if (hm.get(combination) != null) {
                hm.put(combination,hm.get(combination)+1);
                maxPop = Math.max(hm.get(combination),maxPop);
            } else {
                hm.put(combination,1);
                if (maxPop == 0) {
                    maxPop++;
                }
            }
        }

        for (Long c : hm.keySet()) {
            if (hm.get(c) == maxPop) {
                ans += maxPop;
            }
        }
        
        writer.print(ans);
        writer.flush();
    }
}