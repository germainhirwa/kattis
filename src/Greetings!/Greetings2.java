import java.io.*;

public class Greetings2 {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        String hey = sc.readLine();
        
        for (int i = 0; i < hey.length(); i++) {
            writer.print(hey.charAt(i));
            if (hey.charAt(i) == 'e') {
                writer.print('e');
            }
        }

        writer.flush();
    }
}