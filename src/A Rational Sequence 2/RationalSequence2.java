// Tried using Reader class

import java.io.*;
import java.util.*;

public class RationalSequence2 {
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
        
        int n = sc.nextInt();
        while (n-- > 0) {
            int t = sc.nextInt();
            int p = sc.nextInt();
            int q = sc.nextInt();
            List<Boolean> bin = new ArrayList<Boolean>();
            while (p*q != 1) {
                if (p > q) {
                    p -= q;
                    bin.add(true);
                } else {
                    q -= p;
                    bin.add(false);
                }
            }
            bin.add(true);
            int k = 0;
            for (int i = bin.size()-1; i >= 0; i--) {
                k *= 2;
                k += bin.get(i) ? 1 : 0;
            }
            writer.print(t);
            writer.print(" ");
            writer.println(k);
        }
        writer.flush();
    }
}