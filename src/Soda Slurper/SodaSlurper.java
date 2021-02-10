import java.io.*;

public class SodaSlurper {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        String[] line = sc.readLine().split(" ");
        int e = Integer.parseInt(line[0]);
        int f = Integer.parseInt(line[1]);
        int empty = e+f;
        int full = 0;
        int c = Integer.parseInt(line[2]);
        int ans = 0;
        while (empty >= c) {
            full = empty/c;
            empty %= c;
            ans += full;
            empty += full;
            full = 0;
        }
        writer.print(ans);
        writer.flush();
    }
}