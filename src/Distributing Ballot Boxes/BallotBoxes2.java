// Using Reader class to further improve I/O runtime

import java.io.*;
import java.util.*;

public class BallotBoxes6 {
    static class Reader {
        final private int BUFFER_SIZE = 1 << 16;
        private DataInputStream din;
        private byte[] buffer;
        private int bufferPointer, bytesRead;
 
        public Reader()
        {
            din = new DataInputStream(System.in);
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }
 
        public int nextInt() throws IOException
        {
            int ret = 0;
            byte c = read();
            while (c <= ' ') {
                c = read();
            }
            boolean neg = (c == '-');
            if (neg)
                c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
 
            if (neg)
                return -ret;
            return ret;
        }
 
        private void fillBuffer() throws IOException
        {
            bytesRead = din.read(buffer, bufferPointer = 0,
                                 BUFFER_SIZE);
            if (bytesRead == -1)
                buffer[0] = -1;
        }
 
        private byte read() throws IOException
        {
            if (bufferPointer == bytesRead)
                fillBuffer();
            return buffer[bufferPointer++];
        }
    }

    public static void main(String[] args) throws IOException {
        Reader sc = new Reader();
        PrintWriter writer = new PrintWriter(System.out);
        
        while(true) {
            int N = sc.nextInt();

            if (N == -1) { // EOF
                writer.flush();
                return;
            }

            int B = sc.nextInt();

            List<Integer> cities = new ArrayList<Integer>();
            int maxPop = 0, minPop = 1, midPop;
            for (int i = 0; i < N; i++) { // parse everything into the PQ
                // scan n, number of citizens
                // every city must have at least 1 ballot box
                int k = sc.nextInt();
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