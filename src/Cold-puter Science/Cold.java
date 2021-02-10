import java.io.*;

public class Cold {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int queries = Integer.parseInt(sc.readLine());
        String[] line = sc.readLine().split(" ");
        int count = 0;
        for (int i = 0; i < line.length; i++) {
            if (Integer.parseInt(line[i]) < 0) {
                count++;
            }
        }

        writer.print(count);
        writer.flush();
    }
}