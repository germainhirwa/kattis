import java.io.*;

public class SumOfTheOthers {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        while (true) {
            try {
                String[] line = sc.readLine().split(" ");
                int ans = 0;
                for (int i = 0; i < line.length; i++) {
                    ans += Integer.parseInt(line[i]);
                }
                writer.println(ans/2);
            } catch (Exception e) {
                break;
            }
        }

        writer.flush();
    }
}