import java.io.*;

public class Filip {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int a, b, c = 0, d = 0;
        String[] line = sc.readLine().split(" ");
        a = Integer.parseInt(line[0]);
        b = Integer.parseInt(line[1]);

        while (a != 0) {
            c *= 10;
            c += a % 10;
            a /= 10;
        }
        while (b != 0) {
            d *= 10;
            d += b % 10;
            b /= 10;
        }

        writer.print(Math.max(c,d));
        writer.flush();
    }
}