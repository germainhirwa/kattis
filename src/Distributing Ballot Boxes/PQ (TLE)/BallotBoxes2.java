// Still TLE version

import java.io.*;
import java.util.*;

public class BallotBoxes2 {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        BallotComparator bc = new BallotComparator();
        
        while(true) {
            String[] line = sc.readLine().split(" ");
            int N = Integer.parseInt(line[0]);

            if (N == -1) { // EOF
                writer.flush();
                return;
            }

            int B = Integer.parseInt(line[1])-N;

            PriorityQueue<List<Integer>> pq = new PriorityQueue<List<Integer>>(N,bc);
            while (N-- > 0) { // parse everything into the PQ
                // scan n, number of citizens
                // every city must have at least 1 ballot box
                pq.offer(new ArrayList<Integer>(Arrays.asList(Integer.parseInt(sc.readLine()),1))); // pq.add(ballotCount) also fine
            }

            List<Integer> temp;
            while (B-- > 0) { // B-N ballot boxes remaining to allocate
                temp = pq.poll(); // temporary value to be re-inserted later, pq.remove() also fine
                temp.set(1,temp.get(1)+1); // add more ballot box
                pq.add(temp); // re-insert
            }

            // extract the maximum ceil(N/ballot count)
            writer.println((int) Math.ceil(pq.peek().get(0)/((double) pq.peek().get(1)))); // final result
            String blank = sc.readLine(); // skip a line
        }
    }
}

class BallotComparator implements Comparator<List<Integer>> {
    public int compare(List<Integer> b1, List<Integer> b2) {
        return (int) ((((long) b2.get(0))*b1.get(1)) - (((long) b1.get(0))*b2.get(1)));
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