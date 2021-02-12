import java.io.*;
import java.util.*;

public class GrandpaBernie {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int trips = Integer.parseInt(sc.readLine());
        Map<String,List<Integer>> hm = new HashMap<String,List<Integer>>();
        Map<String,Integer> sorted = new HashMap<String,Integer>(); // changed from ArrayList due to TLE

        while (trips-- > 0) { // minimize new variables
            String[] line = sc.readLine().split(" ");
            String country = line[0];
            int year = Integer.parseInt(line[1]);
            if (hm.get(country) != null) {
                hm.get(country).add(year);
            } else {
                List<Integer> years = new ArrayList<Integer>();
                years.add(year);
                hm.put(country,years);
            }
        }

        int queries = Integer.parseInt(sc.readLine());
        while (queries-- > 0) { // minimize new variables
            String[] line = sc.readLine().split(" ");
            String country = line[0];
            int idx = Integer.parseInt(line[1]);
            if (!sorted.containsKey(country)) {
                Collections.sort(hm.get(country));
                sorted.put(country,1);
            }
            writer.println(hm.get(country).get(idx-1));
        }

        writer.flush();
    }
}