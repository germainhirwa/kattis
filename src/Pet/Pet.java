import java.io.*;

public class Pet {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int ans = 0;
        int index = -1;

        for (int i = 0; i < 5; i++) {
            String[] line = sc.readLine().split(" ");
            int s1 = Integer.parseInt(line[0]);
            int s2 = Integer.parseInt(line[1]);
            int s3 = Integer.parseInt(line[2]);
            int s4 = Integer.parseInt(line[3]);
            if (s1+s2+s3+s4 > ans) {
                index = i+1;
                ans = s1+s2+s3+s4;
            }
        }

        writer.print(index);
        writer.print(" ");
        writer.print(ans);
        writer.flush();
    }
}