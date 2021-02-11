import java.io.*;
import java.util.*;

public class Akcija {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        List<Integer> prices = new ArrayList<Integer>();
        int queries = Integer.parseInt(sc.readLine());
        for (int i = 0; i < queries; i++) {
            prices.add(Integer.parseInt(sc.readLine()));
        }
        
        Collections.sort(prices);
        int ans = 0;
        for (int j = queries-1; j >= 0; j--) {
            if (queries-j % 3 != 0) {
                ans += prices.get(j);
            }
        }
        writer.print(ans);
        writer.flush();
    }
}