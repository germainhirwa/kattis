import java.io.*;
import java.util.*;

public class BoatParts {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        String[] line = sc.readLine().split(" ");
        int p = Integer.parseInt(line[0]);
        int d = Integer.parseInt(line[1]);

        Map<String,Integer> hm = new HashMap<String,Integer>();
        for (int i = 0; i < d; i++) {
            String part = sc.readLine();
            if (hm.get(part) == null) {
                hm.put(part,1);
                if (hm.size() == p) {
                    writer.print(i+1);
                    writer.flush();
                    return;
                }
            }
        }

        writer.print("paradox avoided");
        writer.flush();
    }
}