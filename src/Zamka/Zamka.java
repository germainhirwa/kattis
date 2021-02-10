import java.io.*;

public class Zamka {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int l = Integer.parseInt(sc.readLine());
        int d = Integer.parseInt(sc.readLine());
        int x = Integer.parseInt(sc.readLine());
        int minSum = 10001;
        int maxSum = 0;
        for (int i = l; i <= d; i++) {
            int sumDigit = 0;
            int temp = i;
            while (temp > 0) {
                sumDigit += temp % 10;
                temp /= 10;
            }
            if (sumDigit == x && i > maxSum) {
                maxSum = i;
            }
            if (sumDigit == x && i < minSum) {
                minSum = i;
            }
        }

        writer.println(minSum);
        writer.println(maxSum);
        writer.flush();
    }
}