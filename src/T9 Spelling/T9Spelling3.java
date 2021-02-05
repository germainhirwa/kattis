import java.io.*;
import java.util.*;

public class T9Spelling3 {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        int n = Integer.parseInt(sc.readLine());

        Map<String, String> keys = new HashMap<String, String>();
        keys.put("a","2");
        keys.put("b","22");
        keys.put("c","222");
        keys.put("d","3");
        keys.put("e","33");
        keys.put("f","333");
        keys.put("g","4");
        keys.put("h","44");
        keys.put("i","444");
        keys.put("j","5");
        keys.put("k","55");
        keys.put("l","555");
        keys.put("m","6");
        keys.put("n","66");
        keys.put("o","666");
        keys.put("p","7");
        keys.put("q","77");
        keys.put("r","777");
        keys.put("s","7777");
        keys.put("t","8");
        keys.put("u","88");
        keys.put("v","888");
        keys.put("w","9");
        keys.put("x","99");
        keys.put("y","999");
        keys.put("z","9999");
        keys.put(" ","0");

        for (int i = 1; i <= n; i++) {
            String word = sc.readLine();
            String previous = " ";

            // Maybe separating them will help?
            writer.print("Case #");
            writer.print(i);
            writer.print(": ");

            for (int j = 0; j < word.length(); j++) {
                String wk = keys.get(word.substring(j,j+1)); // access the HashMap from j-th letter
                if (previous.equals(wk.substring(0,1))) {
                    writer.print(" "+wk);
                } else {
                    writer.print(wk);
                }
                previous = wk.substring(0,1);
            }
            writer.println();
        }
        writer.flush();
    }
}