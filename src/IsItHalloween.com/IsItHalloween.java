import java.io.*;

public class IsItHalloween {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        String date = sc.readLine();
        writer.print(date.equals("OCT 31") || date.equals("DEC 25") ? "yup" : "nope");

        writer.flush();
    }
}