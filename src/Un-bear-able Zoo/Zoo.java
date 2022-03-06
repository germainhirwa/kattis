import java.io.*;
import java.util.*;

public class Zoo {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int c = 1;
        while (true) {
            int n = Integer.parseInt(sc.readLine());
            if (n == 0) {
                writer.flush();
                break;
            }

            TreeMap<String, Integer> tm = new TreeMap<String, Integer>();
            while (n-- > 0) {
                String[] line = sc.readLine().split(" ");
                String animal = line[line.length - 1].toLowerCase();
                tm.put(animal, 1 + (tm.get(animal) == null ? 0 : tm.get(animal)));
            }

            writer.println("List " + c + ":");
            tm.entrySet().forEach((pair) -> {
                writer.println(pair.getKey() + " | " + pair.getValue());
            });
            c++;
        }
    }
}