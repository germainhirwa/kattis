import java.io.*;
import java.util.*;

public class BallotBoxes4 {
    static class Reader {
        final private int BUFFER_SIZE = 1 << 16;
        private DataInputStream din;
        private byte[] buffer;
        private int bufferPointer, bytesRead;

        public Reader() {
            din = new DataInputStream(System.in);
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }

        public int nextInt() throws IOException {
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

        private void fillBuffer() throws IOException {
            bytesRead = din.read(buffer, bufferPointer = 0,
                                 BUFFER_SIZE);
            if (bytesRead == -1)
                buffer[0] = -1;
        }

        private byte read() throws IOException {
            if (bufferPointer == bytesRead)
                fillBuffer();
            return buffer[bufferPointer++];
        }
    }
    
    public static int ballots(int avg, List<Integer> pops) {
        int ans = 0;
        for (int i : pops) {
            ans += Math.ceil(i/(double) avg);
        }
        return ans;
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
            int maxPop = 0;

            List<Integer> pops = new ArrayList<Integer>();
            while (N-- > 0) {
                // scan n, number of citizens
                int n = sc.nextInt();
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
        }
    }
}
