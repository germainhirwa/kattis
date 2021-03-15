// Finally not a TLE version

import java.io.*;
import java.util.*;

public class BallotBoxes {
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

            List<Integer> cities = new ArrayList<Integer>();
            int maxPop = 0, minPop = 1, midPop;
            for (int i = 0; i < N; i++) { // parse everything into the PQ
                // scan n, number of citizens
                // every city must have at least 1 ballot box
                int k = Integer.parseInt(sc.readLine());
                cities.add(k);
                maxPop = Math.max(k,maxPop);
            }

            while (minPop < maxPop) { // we're going to make it equal
                midPop = (maxPop+minPop)/2;

                int boxes = 0;
                for (int i = 0; i < N; i++) {
                    boxes += (cities.get(i)+midPop-1)/midPop;
                }

                if (boxes > B) {
                    minPop = midPop+1;
                } else {
                    maxPop = midPop;
                }
            }

            // extract the maximum ceil(N/ballot count)
            writer.println(minPop); // final result
            String blank = sc.readLine(); // skip a line
        }
    }
}

/*
Visualization

6 boxes, 4 cities, distribute 2 remaining boxes

120  2680  3400  200
 1    1     1     1     (3400 is the highest, add 1 box)

120  2680  3400  200
 1    1     2     1
120  2680  1700  200    (2680 is the highest, add 1 box)

120  2680  3400  200
 1    2     2     1
120  1340  1700  200    (2 boxes added, highest is 1700)

*/