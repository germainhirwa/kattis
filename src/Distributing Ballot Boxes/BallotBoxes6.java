import java.io.*;
import java.util.*;

public class BallotBoxes6 {
    public static void main(String[] args) throws IOException {
        Reader sc = new Reader();
        PrintWriter writer = new PrintWriter(System.out);
        
        while (true) {
            int N = sc.nextInt();

            if (N == -1) { // EOF
                writer.flush();
                return;
            }

            int B = sc.nextInt();

            int[] cities = new int[N];
            int maxPop = 0, minPop = 1, midPop;
            for (int i = 0; i < N; i++) {
                cities[i] = sc.nextInt() - 1;
                maxPop = Math.max(cities[i] + 1, maxPop);
            }

            while (minPop < maxPop) {
                midPop = (maxPop + minPop) / 2;

                int boxes = 0;
                for (int i = 0; i < N; i++)
                    boxes += (cities[i] + midPop) / midPop;

                if (boxes > B)
                    minPop = midPop + 1;
                else
                    maxPop = midPop;
            }

            writer.println(minPop);
        }
    }

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
}