// Using Reader class

import java.io.*;
import java.util.*;

public class UnionFind {
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

        public String readWord() throws IOException {
            byte[] buf = new byte[1]; // line length
            int cnt = 0, c;
            while ((c = read()) != -1) {
                if (c == ' ') {
                    if (cnt != 0) {
                        break;
                    }
                    else {
                        continue;
                    }
                }
                buf[cnt++] = (byte)c;
            }
            return new String(buf, 0, cnt);
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
        
        int n = sc.nextInt(), t = sc.nextInt();
        UFDS uf = new UFDS(n);
        while (t-- > 0) {
            String q = sc.readWord();
            int a = sc.nextInt(), b = sc.nextInt();
            if (q.equals("=")) {
                uf.unionSet(a,b);
            } else {
                writer.println(uf.isSameSet(a,b) ? "yes" : "no");
            }
        }

        writer.flush();
    }
}

class UFDS {
    public int[] p;
    public int[] rank;

    public UFDS(int N) {
        p = new int[N];
        rank = new int[N];
        for (int i = 0; i < N; i++) {
            p[i] = i;
            rank[i] = 0;
        }
    }

    public int findSet(int i) { 
        if (p[i] == i) return i;
        else return p[i] = findSet(p[i]); 
    }

    public boolean isSameSet(int i, int j) { return findSet(i) == findSet(j); }

    public void unionSet(int i, int j) { 
        if (!isSameSet(i, j)) { 
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