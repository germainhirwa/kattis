import java.io.*;
import java.util.*;

public class Conformity2 {
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

        Map<Long,Integer> hm = new HashMap<Long,Integer>();
        int maxPop = 0;
        int ans = 0;
        
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            long combination = 1L;
            for (int j = 0; j < 5; j++) {
                combination *= (901-sc.nextInt()); // random thought and number
            }
            if (hm.get(combination) != null) {
                hm.put(combination,hm.get(combination)+1);
                maxPop = Math.max(hm.get(combination),maxPop);
            } else {
                hm.put(combination,1);
                if (maxPop == 0) {
                    maxPop++;
                }
            }
        }

        for (Long c : hm.keySet()) {
            if (hm.get(c) == maxPop) {
                ans += maxPop;
            }
        }
        
        writer.print(ans);
        writer.flush();
    }
}