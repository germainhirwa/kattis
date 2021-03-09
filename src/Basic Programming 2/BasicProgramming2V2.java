// Used Reader class for faster I/O

import java.io.*;
import java.util.*;

public class BasicProgramming2V2 {
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

        public long nextLong() throws IOException
        {
            long ret = 0;
            byte c = read();
            while (c <= ' ')
                c = read();
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
        
        int n = sc.nextInt();
        int t = sc.nextInt();

        List<Long> arr = new ArrayList<Long>();
        Map<Long,Integer> hm = new HashMap<Long,Integer>();
        for (int i = 0; i < n; i++) {
            long k = sc.nextLong();
            arr.add(k);
            if (hm.get(k) == null) {
                hm.put(k,1);
            } else {
                hm.put(k,hm.get(k)+1);
            }
        }
        Collections.sort(arr);

        switch (t) {
            case 1:
                int front = 0, back = n-1;
                boolean found = false;
                while (front < back && front < n && back >= 0) {
                    if (arr.get(front)+arr.get(back) == 7777) {
                        found = true;
                        break;
                    } else if (arr.get(front)+arr.get(back) < 7777) {
                        front++;
                    } else {
                        back--;
                    }
                }
                writer.println(found ? "Yes" : "No");
                break;
            case 2:
                boolean unique = true;
                for (int c : hm.values()) {
                    if (c != 1) {
                        unique = false;
                        break;
                    }
                }
                writer.println(unique ? "Unique" : "Contains duplicate");
                break;
            case 3:
                boolean found2 = false;
                for (Long c : hm.keySet()) {
                    if (hm.get(c) > n/2) {
                        writer.println(c);
                        found2 = true;
                        break;
                    }
                }
                if (!found2) {
                    writer.println(-1);
                }
                break;
            case 4:
                if (n % 2 == 0) {
                    writer.print(arr.get(n/2-1));
                    writer.print(" ");
                    writer.print(arr.get(n/2));
                } else {
                    writer.println(arr.get(n/2));
                }
                break;
            case 5:
                for (long i : arr) {
                    if (100 <= i && i <= 999) {
                        writer.print(i);
                        writer.print(" ");
                    }
                }
                break;
        }

        writer.flush();
    }
}