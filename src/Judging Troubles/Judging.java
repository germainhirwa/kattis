import java.io.*;
import java.util.*;

public class Judging {
    /* public static int haslineode(String s) {
        return ((int) s.charAt(0)) + ((int) s.charAt(1));
    } */

    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);

        Map<String,Integer> dom = new HashMap<String,Integer>();
        Map<String,Integer> kattis = new HashMap<String,Integer>();
        
        int n = Integer.parseInt(sc.readLine()), ans = 0;
        String line;
        for (int i = 0; i < n; i++) {
            line = sc.readLine();
            if (dom.get(line) == null)
                dom.put(line,1);
            else
                dom.put(line,dom.get(line)+1);
        }
        for (int i = 0; i < n; i++) {
            line = sc.readLine();
            if (kattis.get(line) == null)
                kattis.put(line,1);
            else
                kattis.put(line,kattis.get(line)+1);
        }
        for (String k : dom.keySet()) {
            if (kattis.get(k) != null)
                ans += Math.min(dom.get(k),kattis.get(k));
        }
        writer.print(ans);
        writer.flush();
    }
}