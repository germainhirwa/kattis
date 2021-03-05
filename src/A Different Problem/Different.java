import java.io.*;

public class Different {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        try {
            while (true) {
                String[] line = sc.readLine().split(" ");
                long a = Long.parseLong(line[0]);
                long b = Long.parseLong(line[1]);
                writer.println(Math.abs(a-b));   
            }
        } catch (Exception e) {
            writer.flush();
        }
    }
}