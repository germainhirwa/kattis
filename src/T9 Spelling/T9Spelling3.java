// The most improved version of T9Spelling

import java.io.*;
import java.util.*;

public class T9Spelling3 {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        int n = Integer.parseInt(sc.readLine());

        Map<Integer, Integer> keys = new HashMap<Integer, Integer>(); // create a HashMap
        keys.put(97,2); // put every ASCII key and number, avoid String to improve time running
        keys.put(98,22);
        keys.put(99,222);
        keys.put(100,3);
        keys.put(101,33);
        keys.put(102,333);
        keys.put(103,4);
        keys.put(104,44);
        keys.put(105,444);
        keys.put(106,5);
        keys.put(107,55);
        keys.put(108,555);
        keys.put(109,6);
        keys.put(110,66);
        keys.put(111,666);
        keys.put(112,7);
        keys.put(113,77);
        keys.put(114,777);
        keys.put(115,7777);
        keys.put(116,8);
        keys.put(117,88);
        keys.put(118,888);
        keys.put(119,9);
        keys.put(120,99);
        keys.put(121,999);
        keys.put(122,9999);
        keys.put(32,0);

        for (int i = 1; i <= n; i++) {
            String word = sc.readLine();
            int previous = -1; // set an impossible value

            // Separating them will help to avoid concatenation
            writer.print("Case #");
            writer.print(i);
            writer.print(": ");

            for (int j = 0; j < word.length(); j++) { // iterate every letter in the word
                int wk = keys.get((int) word.charAt(j)); // access the HashMap from j-th letter
                if (previous == wk%10) { // compare the last digit because it's always the same as the first digit
                    writer.print(" "); // add whitespace
                }
                writer.print(wk);
                previous = wk%10; // replace previous
            }
            writer.println();
        }
        writer.flush();
    }
}