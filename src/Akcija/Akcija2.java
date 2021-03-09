// Using Reader class to further improve I/O runtime

import java.io.*;
import java.util.*;

public class Akcija2 {
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

            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');

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
        
        List<Integer> prices = new ArrayList<Integer>();
        int queries = sc.nextInt();
        for (int i = 0; i < queries; i++) {
            prices.add(sc.nextInt());
        }
        
        Collections.sort(prices);
        int ans = 0;
        for (int j = queries-1; j >= 0; j--) {
            if ((queries-j) % 3 != 0) {
                ans += prices.get(j);
            }
        }
        writer.print(ans);
        writer.flush();
    }
}