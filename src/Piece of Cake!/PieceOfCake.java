import java.io.*;

public class PieceOfCake {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        String[] line = sc.readLine().split(" ");
        int n = Integer.parseInt(line[0]);
        int h = Integer.parseInt(line[1]);
        int v = Integer.parseInt(line[2]);

        writer.print(Math.max(h,n-h)*Math.max(v,n-v)*4);
        writer.flush();
    }
}