// Using Reader class for faster I/O

import java.io.*;
import java.util.*;

public class WeakVertices2 {
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
        
        while (true) {
            int n = sc.nextInt();
            if (n == -1) {
                writer.flush();
                return;
            } else if (n < 3) {
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        int dummy = sc.nextInt();
                    }
                    writer.print(i);
                    writer.print(" ");
                }
                writer.println();
            } else {
                List<Integer> weakList = new ArrayList<Integer>();
                int[][] arr = new int[n][n];
                boolean[] found = new boolean[n];
                for (int i = 0; i < n; i++) {
                    found[i] = false;
                    for (int j = 0; j < n; j++) {
                        arr[i][j] = sc.nextInt();
                    }
                }

                // Improving this part somehow gives WA, so I'll just stick to this for now
                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        for (int k = 0; k < n; k++) {
                            if (arr[i][j]*arr[i][k]*arr[j][k] == 1) {
                                found[i] = true;
                                found[j] = true;
                                found[k] = true;
                                break;
                            }
                        }
                    }
                    if (!found[i]) {
                        weakList.add(i);
                    }
                }

                for (int i : weakList) {
                    writer.print(i);
                    writer.print(" ");
                }
                writer.println();
            }
        }
    }
}