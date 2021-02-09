import java.io.*;

public class Faktor {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        String[] line = sc.readLine().split(" ");
        writer.println(Integer.parseInt(line[0])*(Integer.parseInt(line[1])-1)+1);

        writer.flush();
    }
}