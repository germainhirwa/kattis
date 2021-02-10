import java.io.*;

public class ElectricalOutlets {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int queries = Integer.parseInt(sc.readLine());
        for (int i = 0; i < queries; i++) {
            String[] line = sc.readLine().split(" ");
            int ans = 1;
            for (int j = 1; j < line.length; j++) {
                ans += Integer.parseInt(line[j])-1;
            }
            writer.println(ans);
        }

        writer.flush();
    }
}