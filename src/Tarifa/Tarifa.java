import java.io.*;

public class Tarifa {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int x = Integer.parseInt(sc.readLine());
        int n = Integer.parseInt(sc.readLine());
        int ans = x*(n+1);
        for (int i = 0; i < n; i++) {
            ans -= Integer.parseInt(sc.readLine());
        }
        writer.print(ans);
        writer.flush();
    }
}