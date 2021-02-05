import java.io.*;
import java.util.*;

public class SortOfSorting {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        int num = -1; // default value
        boolean flag = false; // to check whether it's the first input for blank spaces management
        while (num != 0) {
            num = Integer.parseInt(sc.readLine());
            if (flag) {
                writer.println();
            }
            if (num == 0) {
                break;
            }
            List<String> names = new ArrayList<>();
            for (int i = 0; i < num; i++) {
                names.add(sc.readLine());
            }
            Collections.sort(names, new Comparator<String>() {
                public int compare(String name1, String name2) {
                    return (name1.substring(0,2)).compareTo(name2.substring(0,2));
                }
            });
            for (int i = 0; i < num; i++) {
                writer.println(names.get(i));
            }
            flag = true;
        }
        writer.flush();
    }
}