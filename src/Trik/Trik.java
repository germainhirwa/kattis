import java.io.*;
import java.util.*; // only if using List ADT

public class Trik {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        String line = sc.readLine();
        int ans = 1;
        for (int i = 0; i < line.length(); i++) {
            if (line.charAt(i)=='A' && ans != 3) {
                ans = 3-ans;
            } else if (line.charAt(i)=='B' && ans != 1) {
                ans = 5-ans;
            } else if (line.charAt(i)=='C' && ans != 2) {
                ans = 4-ans;
            }
        }
        writer.print(ans);
        writer.flush();
    }
}