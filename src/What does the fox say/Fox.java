import java.io.*;
import java.util.*;

public class Fox {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int queries = Integer.parseInt(sc.readLine());

        for (int i = 0; i < queries; i++) {
            String[] recording = sc.readLine().split(" ");
            List<String> otherAnimals = new ArrayList<String>();
            String input = "";
            while (true) {
                input = sc.readLine();
                if (input.contains("fox")) {
                    break;
                }
                String[] animal = input.split("goes ");
                otherAnimals.add(animal[1]);
            }
            for (String s : recording) {
                if (!otherAnimals.contains(s)) {
                    writer.print(s);
                    writer.print(" ");
                }
            }
            writer.println();
        }

        writer.flush();
    }
}