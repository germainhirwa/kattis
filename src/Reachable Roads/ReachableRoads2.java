// Using Reader class, with UFDS

import java.io.*;
import java.util.*;

public class ReachableRoads2 {
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
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
            return ret;
        }

        private byte read() throws IOException {
            if (bufferPointer == bytesRead) {
                bytesRead = din.read(buffer, bufferPointer = 0,
                                    BUFFER_SIZE);
                if (bytesRead == -1)
                    buffer[0] = -1;
            }
            return buffer[bufferPointer++];
        }
    }

    public static void main(String[] args) throws IOException {
        Reader sc = new Reader();
        PrintWriter writer = new PrintWriter(System.out);
        
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt(), q = sc.nextInt();
            UFDS uf = new UFDS(n);
            while (q-- > 0)
                uf.unionSet(sc.nextInt(),sc.nextInt());
            
            writer.println(uf.numSets-1);
        }

        writer.flush();
    }
}

class UFDS {
    public int[] p;
    public int[] rank;
    public int numSets;

    public UFDS(int N) {
        p = new int[N];
        rank = new int[N];
        for (int i = 0; i < N; i++) {
            p[i] = i;
            rank[i] = 0;
        }
        numSets = N;
    }

    public int findSet(int i) {
        if (p[i] == i) return i;
        else return p[i] = findSet(p[i]);
    }

    public boolean isSameSet(int i, int j) { return findSet(i) == findSet(j); }

    public void unionSet(int i, int j) {
        if (!isSameSet(i, j)) {
            numSets--;
            int x = findSet(i), y = findSet(j);
            if (rank[x] > rank[y])
                p[y] = x;
            else { 
                p[x] = y;
                if (rank[x] == rank[y])
                    rank[y] = rank[y]++;
            } 
        } 
    }
}