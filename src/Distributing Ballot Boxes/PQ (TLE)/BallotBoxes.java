// TLE Version

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
            PriorityQueue pq = new PriorityQueue();
            for (int i = 0; i < N; i++) { // parse everything into the PQ
                long[] ballotCount = new long[2];
                ballotCount[1] = 1; // every city must have at least 1 ballot box
                ballotCount[0] = Long.parseLong(sc.readLine()); // scan n, number of citizens
                pq.insert(ballotCount);
            }

            for (int i = 0; i < B-N; i++) { // B-N ballot boxes remaining to allocate
                long[] temp = pq.extractMax(); // temporary value to be re-inserted later
                temp[1]++; // add more ballot box
                pq.insert(temp); // re-insert
            }

            long[] best = pq.extractMax(); // extract the maximum ceil(N/ballot count)
            writer.println((int) Math.ceil(best[0]/((double) best[1]))); // final result
            String blank = sc.readLine();
        }
    }
}

// Priority Queue with elements {N, ballot count}. Priority based on ceil(N/ballot count)
class PriorityQueue {
    public ArrayList<long[]> A;
    public int PriorityQueueSize;

    PriorityQueue() {
        A = new ArrayList<long[]>();
        A.add(new long[2]);
        PriorityQueueSize = 0;
    }

    int parent(int i) { return i>>1; }
    int left(int i) { return i<<1; }
    int right(int i) { return (i<<1) + 1; }

    void shiftUp(int i) {
        while (i > 1 && Math.ceil(A.get(parent(i))[0]/((double) A.get(parent(i))[1])) < Math.ceil(A.get(i)[0]/((double) A.get(i)[1]))) {
            long[] temp = A.get(i);
            A.set(i, A.get(parent(i)));
            A.set(parent(i), temp);
            i = parent(i);
        }
    }

    void insert(long[] key) {
        PriorityQueueSize++;
        if (PriorityQueueSize >= A.size())
            A.add(key);
        else
            A.set(PriorityQueueSize, key);
        shiftUp(PriorityQueueSize);
    }

    void shiftDown(int i) {
        while (i <= PriorityQueueSize) {
            long[] maxV = A.get(i);
            int max_id = i;

            // compare value of this node with its left subtree, if possible
            if (left(i) <= PriorityQueueSize && Math.ceil(maxV[0]/((double) maxV[1])) < Math.ceil(A.get(left(i))[0]/((double) A.get(left(i))[1]))) { 
                maxV = A.get(left(i));
                max_id = left(i);
            }
            // now compare with its right subtree, if possible
            if (right(i) <= PriorityQueueSize && Math.ceil(maxV[0]/((double) maxV[1])) < Math.ceil(A.get(right(i))[0]/((double) A.get(right(i))[1]))) {
                // maxV = A.get(right(i));
                max_id = right(i);
            }

            if (max_id != i) {
                long[] temp = A.get(i);
                A.set(i, A.get(max_id));
                A.set(max_id, temp);
                i = max_id;
            }
            else
                break;
        }
    }
  
    long[] extractMax() {
        long[] maxV;
        if (PriorityQueueSize != 0) {
            maxV = A.get(1);    
            A.set(1, A.get(PriorityQueueSize));
            PriorityQueueSize--; // virtual decrease
            shiftDown(1);
        }
        return maxV;
    }

    int size() { return PriorityQueueSize; }
    boolean isEmpty() { return PriorityQueueSize == 0; }
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