import java.io.*;
import java.util.*;

public class BallotBoxes3 {
    public static int ballots(int avg, List<Integer> pops) {
        int ans = 0;
        for (int i : pops) {
            ans += Math.ceil(i/(double) avg);
        }
        return ans;
    }
    
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        while(true) {
            String[] line = sc.readLine().split(" ");
            int N = Integer.parseInt(line[0]);

            if (N == -1) { // EOF
                writer.flush();
                return;
            }

            int B = Integer.parseInt(line[1]);
            int maxPop = 0;

            List<Integer> pops = new ArrayList<Integer>();
            while (N-- > 0) {
                // scan n, number of citizens
                int n = Integer.parseInt(sc.readLine());
                maxPop = Math.max(maxPop,n);
                pops.add(n);
            }
            
            int hi = maxPop, lo = 1;
            
            // Binary search
            while (lo + 1 != hi) {
                int mid = (hi+lo)/2;
                if (ballots(mid,pops) > B)
                    lo = mid;
                else // < B
                    hi = mid;
            }
            writer.println(lo+1);

            String blank = sc.readLine();
        }
    }
}
