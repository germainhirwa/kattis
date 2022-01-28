import java.io.*;
import java.util.*;

public class Han {
    public static void main(String[] args) throws IOException {
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter writer = new PrintWriter(System.out);
        
        int n = Integer.parseInt(sc.readLine());
        int time = 0;
        int pos = 0;
        int[] arr = new int[26];
        boolean fwd = true;
        while (n-- > 0) {
            String[] line = sc.readLine().split(" ");
            int next = Integer.parseInt(line[1]);
            for (int i = time % 26; i < 26; i++) {
                arr[pos]++;
                pos = fwd ? (pos + 1) % 26 : (pos + 25) % 26;
            }
            for (int i = 0; i < next % 26; i++) {
                arr[pos]++;
                pos = fwd ? (pos + 1) % 26 : (pos + 25) % 26;
            }
            int inc = ((next - next % 26) - (time - time % 26)) / 26 - 1;
            for (int i = 0; i < 26; i++) {
                arr[i]+= inc;
            }
            if (line[0].equals("UPIT")) {
                int idx = line[2].charAt(0) - 97;
                writer.println(arr[idx]);
            } else {
                fwd = !fwd;
                pos = fwd ? (pos + 2) % 26 : (pos + 24) % 26;
            }
            time = next;
        }
        writer.flush();
    }
}