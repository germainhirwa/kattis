import java.io.*;
import java.util.*;

public class EmPleh {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        String line1 = sc.readLine();
        String[] white = line1.substring(7,line1.length()).split(",");
        String line2 = sc.readLine();
        String[] black = line2.substring(7,line2.length()).split(",");

        Map<String,Character> hm = new HashMap<String,Character>();

        for (int w = 0; w < white.length; w++) {
            if (white[w].length() == 3) {
                hm.put(white[w].substring(1,3),white[w].charAt(0));
            } else {
                hm.put(white[w],'P');
            }
        }

        for (int b = 0; b < black.length; b++) {
            if (black[b].length() == 3) {
                hm.put(black[b].substring(1,3),Character.toLowerCase(black[b].charAt(0)));
            } else {
                hm.put(black[b],'p');
            }
        }

        String[] alphabets = {"a", "b", "c", "d", "e", "f", "g", "h"};

        writer.println("+---+---+---+---+---+---+---+---+");
        for (int row = 8; row >= 1; row--) {
            for (int col = 0; col < 8; col++) {
                writer.print("|");
                if ((row+col) % 2 == 0) {
                    writer.print('.');
                    if (hm.get(alphabets[col]+row) != null) {
                        writer.print(hm.get(alphabets[col]+row));
                    } else {
                        writer.print('.');
                    }
                    writer.print('.');
                } else {
                    writer.print(':');
                    if (hm.get(alphabets[col]+row) != null) {
                        writer.print(hm.get(alphabets[col]+row));
                    } else {
                        writer.print(':');
                    }
                    writer.print(':');
                }
            }
            writer.println("|");
            writer.println("+---+---+---+---+---+---+---+---+");
        }

        /*
        writer.println();
        writer.println(Arrays.toString(white));
        writer.println(Arrays.toString(black));
        */
        writer.flush();
    }
}