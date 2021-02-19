// Still TLE version

import java.io.*;
import java.util.*;

// This time using City object
public class BallotBoxes3 {
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

            PriorityQueue<City> pq = new PriorityQueue<City>(N,bc);
            while (N-- > 0) { // parse everything into the PQ
                // scan n, number of citizens
                // every city must have at least 1 ballot box
                pq.offer(new City(Integer.parseInt(sc.readLine()))); // pq.add(ballotCount) also fine
            }

            City temp;
            while (B-- > 0) { // B-N ballot boxes remaining to allocate
                temp = pq.poll(); // temporary value to be re-inserted later, pq.remove() also fine
                temp.ballot++; // add more ballot box
                pq.add(temp); // re-insert
            }

            // extract the maximum ceil(N/ballot count)
            writer.println((int) Math.ceil(pq.peek().population/((double) pq.peek().ballot))); // final result
            String blank = sc.readLine(); // skip a line
        }
    }
}

class City {
    public int population;
    public int ballot;

    public City(int population) {
        this.population = population;
        this.ballot = 1;
    }

    public City(int population, int ballot) {
        this.population = population;
        this.ballot = ballot;
    }
}

class BallotComparator implements Comparator<City> {
    public int compare(City c1, City c2) {
        return (int) ((((long) c2.population)*c1.ballot) - (((long) c1.population)*c2.ballot));
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