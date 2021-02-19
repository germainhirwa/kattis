// TLE but as intuitive as possible

import java.io.*;
import java.util.*;

public class JoinStrings {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        List<String> strings = new ArrayList<String>();
        Map<Integer,List<Integer>> indexes = new HashMap<Integer,List<Integer>>();

        int queries = Integer.parseInt(sc.readLine());
        int flag = queries;
        int lastIndex = 0;
        
        for (int i = 0; i < queries; i++) {
            strings.add(sc.readLine());
            indexes.put(i,new ArrayList<Integer>(Arrays.asList(i)));
        }

        for (int j = 0; j < queries-1; j++, flag--) {
            String[] nums = sc.readLine().split(" ");
            int n1 = Integer.parseInt(nums[0])-1;
            int n2 = Integer.parseInt(nums[1])-1;
            indexes.get(n1).addAll(indexes.get(n2));
            indexes.get(n2).clear();
            if (flag == 2) {
                lastIndex = n1;
            }
        }
        
        for (int k = 0; k < queries; k++) {
            writer.print(strings.get(indexes.get(lastIndex).get(k)));
        }

        writer.flush();
    }
}