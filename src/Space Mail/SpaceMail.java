import java.io.*;
import java.util.*;

class UnionFind {
    public int[] p;
    public int[] rank;
    public int numSets;

    public UnionFind(int N) {
        p = new int[N];
        rank = new int[N];
        numSets = N;
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
            numSets--;
            int x = findSet(i), y = findSet(j);
            // rank is used to keep the tree short
            if (rank[x] > rank[y])
                p[y] = x;
            else {
                p[x] = y;
                if (rank[x] == rank[y])
                    rank[y] = rank[y]+1;
            } 
        } 
    }

    public int numDisjointSets() { return numSets; }
}

public class SpaceMail {
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
    
    public static void main(String[] args) throws IOException {
        Reader sc = new Reader();
        PrintWriter writer = new PrintWriter(System.out);
        
        int n = sc.nextInt();
        Map<Long, Integer> rev = new HashMap<Long, Integer>();
        Map<Long, List<Long>> dists = new HashMap<Long, List<Long>>();
        List<Long> arr = new ArrayList<Long>();
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            int z = sc.nextInt();
            long p1 = 1002001 * x + 1001 * y + z;
            for (long p2 : rev.keySet()) {
                long dist = (p1 % 1001 - p2 % 1001) * (p1 % 1001 - p2 % 1001) +
                        (p1 / 1001 % 1001 - p2 / 1001 % 1001) * (p1 / 1001 % 1001 - p2 / 1001 % 1001) +
                        (p1 / 1002001 % 1001 - p2 / 1002001 % 1001) * (p1 / 1002001 % 1001 - p2 / 1002001 % 1001);
                if (dists.get(dist) == null) {
                    dists.put(dist, new ArrayList<Long>());
                    arr.add(dist);
                }
                dists.get(dist).add(1003003001 * p1 + p2);
            }
            rev.put(p1, i);
        }

        Collections.sort(arr);

        // Kruskal's Algorithm, slightly modified
        UnionFind ufds = new UnionFind(n);
        long minmax = 0;
        for (long d : arr) {
            for (long h : dists.get(d)) {
                long q1 = h / 1003003001;
                long q2 = h % 1003003001;
                if (!ufds.isSameSet(rev.get(q1), rev.get(q2))) {
                    minmax = Math.max(minmax, d);
                    ufds.unionSet(rev.get(q1), rev.get(q2));
                }
                if (ufds.numDisjointSets() == 1) {
                    writer.println((int) Math.ceil(Math.pow(minmax, 0.5)));
                    writer.flush();
                    System.exit(0);
                }
            }
        }
    }
}