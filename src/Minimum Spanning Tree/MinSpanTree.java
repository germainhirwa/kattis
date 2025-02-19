// Using Reader class
import java.io.*;
import java.util.*;

public class MinSpanTree {
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
        
        while (true) {
            int n = sc.nextInt();
            int m = sc.nextInt();
            if (n == 0 && m == 0) {
                writer.flush();
                return;
            }

            EdgeList graph = new EdgeList(n);
            for (int i = 0; i < m; i++) {
                graph.connect(sc.nextInt(),sc.nextInt(),sc.nextInt());
            }

            List<Triple> mst = graph.MST();
            if (mst.size() != n-1)
                writer.println("Impossible");
            else {
                int cost = 0;
                Collections.sort(mst);
                for (Triple t : mst)
                    cost += t.third;
                writer.println(cost);
                for (Triple t : mst)
                    writer.println(t.first+" "+t.second);
            }
        }
    }
}

class EdgeList {
    public List<Triple> list;
    public int numVertices;

    public EdgeList (int V) {
        numVertices = V;
        list = new ArrayList<Triple>();
    }

    public void connect (int a, int b, int w) {
        list.add(new Triple(Math.min(a,b),Math.max(a,b),w));
    }

    public List<Triple> MST () {
        UnionFind ufds = new UnionFind(numVertices);
        KruskalComparator kc = new KruskalComparator();
        list.sort(kc);

        List<Triple> mst = new ArrayList<Triple>();
        for (int i = 0; i < list.size(); i++) {
            if (!ufds.isSameSet(list.get(i).first,list.get(i).second)) {
                mst.add(list.get(i));
                ufds.unionSet(list.get(i).first,list.get(i).second);
            }
            if (ufds.numDisjointSets() == 1) { // all vertices inside MST
                break;
            }
        }

        return mst;
    }
}

class Triple implements Comparable<Triple> {
    public int first;
    public int second;
    public int third;

    public Triple (int a, int b, int w) {
        first = a;
        second = b;
        third = w;
    }

    @Override
    public int compareTo (Triple other) {
        if (this.first != other.first)
            return this.first - other.first;
        else
            return this.second - other.second;
    }
}

class KruskalComparator implements Comparator<Triple> {
    public int compare (Triple t1, Triple t2) {
        if (t1.third == t2.third) {
            if (t1.first == t2.first)
                return t1.second - t2.second;
            else
                return t1.first - t1.first;
        } else
            return t1.third - t2.third;
    }
}

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