import java.io.*;

public class DiceCup {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        String[] line = sc.readLine().split(" ");
        int m = Integer.parseInt(line[0]);
        int n = Integer.parseInt(line[1]);

        for (int i = Math.min(m,n)+1; i <= Math.max(m,n)+1; i++) {
            writer.println(i);
        }

        writer.flush();
    }
}