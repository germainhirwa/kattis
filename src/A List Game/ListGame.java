import java.io.*;

public class ListGame {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int n = Integer.parseInt(sc.readLine());
        int k = 0, i = 2;
        while (i*i <= n) {
            if (n % i == 0) {
                n /= i;
                k++;
            } else {
                i ++;
            }
        }
        writer.println(k + (n == 1 ? 0 : 1));
        writer.flush();
    }
}