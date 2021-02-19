// Still TLE version

import java.io.*;
import java.util.*;

// This time using City object
public class BallotBoxes4 {
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

            int B = Integer.parseInt(line[1])-N;

            PriorityQueue pq = new PriorityQueue();
            while (N-- > 0) { // parse everything into the PQ
                // scan n, number of citizens
                // every city must have at least 1 ballot box
                pq.insert(new City(Integer.parseInt(sc.readLine())));
            }

            City temp;
            while (B-- > 0) { // B-N ballot boxes remaining to allocate
                pq.A.get(1).ballot++; // increment the root's ballot boxes by 1
                pq.shiftDown(1); // shift down
            }

            // extract the maximum ceil(N/ballot count)
            City best = pq.A.get(1);
            writer.println((int) Math.ceil(best.population/((double) best.ballot))); // final result
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

    public int rank() {
        return (int) Math.ceil(this.population/((double) this.ballot));
    }
}

class PriorityQueue {
    public ArrayList<City> A;
    public int PriorityQueueSize;

    PriorityQueue() {
        A = new ArrayList<City>();
        A.add(null);
        PriorityQueueSize = 0;
    }

    int parent(int i) { return i>>1; }
    int left(int i) { return i<<1; }
    int right(int i) { return (i<<1) + 1; }

    void shiftUp(int i) {
        while (i > 1 && A.get(parent(i)).rank() < A.get(i).rank()) {
            City temp = A.get(i);
            A.set(i, A.get(parent(i)));
            A.set(parent(i), temp);
            i = parent(i);
        }
    }

    void insert(City key) {
        PriorityQueueSize++;
        if (PriorityQueueSize >= A.size())
            A.add(key);
        else
            A.set(PriorityQueueSize, key);
        shiftUp(PriorityQueueSize);
    }

    void shiftDown(int i) {
        while (i <= PriorityQueueSize) {
            City maxV = A.get(i);
            int max_id = i;

            // compare value of this node with its left subtree, if possible
            if (left(i) <= PriorityQueueSize && maxV.rank() < A.get(left(i)).rank()) { 
                maxV = A.get(left(i));
                max_id = left(i);
            }
            // now compare with its right subtree, if possible
            if (right(i) <= PriorityQueueSize && maxV.rank() < A.get(right(i)).rank()) {
                max_id = right(i);
            }

            if (max_id != i) {
                City temp = A.get(i);
                A.set(i, A.get(max_id));
                A.set(max_id, temp);
                i = max_id;
            }
            else
                break;
        }
    }

    int size() { return PriorityQueueSize; }
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