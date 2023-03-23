import java.io.*;
import java.util.*;

public class ShatteredCake {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        Map<String, Integer> hashMap = new HashMap<String, Integer>();
        
        int w = Integer.parseInt(sc.readLine());
        int n = Integer.parseInt(sc.readLine());
        int area = 0;
        
        while (n-- > 0) {
            String nums = sc.readLine();
            try {
                area += hashMap.get(nums);
            } catch (Exception e) {
                hashMap.put(nums,Integer.parseInt(nums.split(" ")[0])*Integer.parseInt(nums.split(" ")[1]));
                area += hashMap.get(nums);
            }
        }
        
        writer.print(area/w);
        writer.flush();
    }
}