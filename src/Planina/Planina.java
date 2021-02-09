import java.io.*;

public class Planina {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int n = Integer.parseInt(sc.readLine());
        writer.println(Math.round(Math.pow(Math.pow(2,n)+1,2)));
        writer.flush();
    }
}