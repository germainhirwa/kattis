// The term 'other drawer' refers to the drawers in A's and B's set only, not a stack
// Using Reader class to further improve I/O runtime

import java.io.*;
import java.util.*;

public class Ladice2 {
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
        
        int N = sc.nextInt();
        int L = sc.nextInt();
        UnionFind ufds = new UnionFind(L);
        while (N-- > 0) {
            int A = sc.nextInt()-1;
            int B = sc.nextInt()-1;
            ufds.unionSet(A,B);

            // The 2 first rules are equivalent considering the UFDS algorithm, and so are the 2 last rules
            int parentA = ufds.findSet(A);
            if (ufds.fill[parentA] != 0) {
                ufds.fill[parentA]--;
                writer.println("LADICA");
            } else {
                writer.println("SMECE");
            }
            /*
            writer.println(A+" "+B);
            writer.println(Arrays.toString(ufds.p));
            */
        }

        writer.flush();
    }
}

class UnionFind {
    public int[] p;
    public int[] rank;
    public int numSets;
    public int[] fill; // number of items in itself and nodes below it

    public UnionFind(int N) {
        p = new int[N];
        rank = new int[N];
        fill = new int[N];
        numSets = N;
        for (int i = 0; i < N; i++) {
            p[i] = i;
            rank[i] = 0;
            fill[i] = 1;
        }
    }

    public int findSet(int i) { 
        if (p[i] == i) return i;
        else {
            p[i] = findSet(p[i]);
            return p[i]; 
        } 
    }

    public Boolean isSameSet(int i, int j) { return findSet(i) == findSet(j); }

    public void unionSet(int i, int j) { 
        if (!isSameSet(i, j)) { 
            numSets--; 
            int x = findSet(i), y = findSet(j);
            if (rank[x] > rank[y]) {
            	p[y] = x;
                fill[x] += fill[y];
            } else { 
            	p[x] = y;
                if (rank[x] == rank[y]) {
                    rank[y] = rank[y]++;
                    fill[y] += fill[x];
                }
            } 
        } 
    }
}