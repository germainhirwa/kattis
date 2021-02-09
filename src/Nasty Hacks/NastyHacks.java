import java.io.*;

public class NastyHacks {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int queries = Integer.parseInt(sc.readLine());
        
        for (int i = 0; i < queries; i++) {
            String[] line = sc.readLine().split(" ");
            int r = Integer.parseInt(line[0]);
            int e = Integer.parseInt(line[1]);
            int c = Integer.parseInt(line[2]);

            if (e-r < c) {
                writer.println("do not advertise");
            } else if (e-r == c) {
                writer.println("does not matter");
            } else {
                writer.println("advertise");
            }
        }

        writer.flush();
    }
}