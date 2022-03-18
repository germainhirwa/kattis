import java.io.*;
import java.util.*;

class AdjacencyList {
    public List<List<Pair>> list;
    public int numVertices;
    public boolean directed;
    public double[] D; // for SSSP

    public AdjacencyList (int V, boolean dir) {
        directed = dir;
        numVertices = V;
        list = new ArrayList<List<Pair>>();
        for (int i = 0; i < V; i++)
            list.add(new ArrayList<Pair>());
    }

    public void connect (int a, int b) { // unweighted graph
        connect(a,b,1);
    }

    public void connect (int a, int b, double w) { // weighted graph
        list.get(a).add(new Pair(b,w));
        if (!directed) {
            list.get(b).add(new Pair(a,w));
        }
    }

    // If the path is needed, just backtrack from parent
    public void initSSSP (int s) {
        D = new double[numVertices];
        for (int i = 0; i < numVertices; i++)
            D[i] = Double.MAX_VALUE;
        D[s] = 0;
    }

    public void relax (int u, int v, double w) {
        if (D[u] != Double.MAX_VALUE && D[v] > D[u] + w) { // if SP can be shortened
            D[v] = D[u] + w; // relax this edge
        }
    }

    public double SSSPDijkstra (int s, int t) { // Modified Dijkstra's Algorithm
        initSSSP(s);

        PrimComparator pc = new PrimComparator(); // The comparator is the same for Prim's (sort by weight then by dest)
        PriorityQueue<Pair> pq = new PriorityQueue<Pair>(pc);
        pq.offer(new Pair(s,0)); // recall my version of Pair is (dest, weight) not (weight, dest)

        while (!pq.isEmpty()) {
            Pair ud = pq.poll();
            if (ud.second == D[ud.first]) { // important check, lazy DS
                for (Pair e : list.get(ud.first)) {
                    if (D[e.first] > D[ud.first] + e.second) { // can relax
                        relax(ud.first, e.first, e.second); // relax
                        pq.offer(new Pair(e.first,D[e.first]));
                    }
                }
            }
        }

        return D[t];
    }
}

class Pair implements Comparable<Pair> {
    // This is how we access the elements of the pair, just like in C++
    public int first;
    public double second;

    public Pair (int v, double w) {
        first = v;
        second = w;
    }

    @Override
    public int compareTo (Pair other) {
        if (this.first != other.first)
            return this.first - other.first;
        else
            return (this.second > other.second) ? 1 : ((this.second < other.second) ? -1 : 0);
    }
}

class PrimComparator implements Comparator<Pair> {
    public int compare (Pair p1, Pair p2) {
        if (p1.second == p2.second)
            return p1.first - p2.first;
        else
            return (p1.second > p2.second) ? 1 : ((p1.second < p2.second) ? -1 : 0);
    }
}

public class GetShorty {
    public static void main(String[] args) throws IOException {
        Reader sc = new Reader();
        PrintWriter writer = new PrintWriter(System.out);

        while (true) {
            int n = sc.nextInt(), m = sc.nextInt();
            if (n == 0 && m == 0) {
                writer.flush();
                return;
            }

            AdjacencyList al = new AdjacencyList(n, false);
            while(m-- > 0) {
                al.connect(sc.nextInt(), sc.nextInt(), -Math.log(sc.nextDouble()));
            }

            writer.printf("%.4f\n", Math.exp(-al.SSSPDijkstra(0, n - 1)));
        }
    }

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

        public double nextDouble() throws IOException {
            double ret = 0, div = 1;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)
                c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
            if (c == '.') {
                while ((c = read()) >= '0' && c <= '9') {
                    ret += (c - '0') / (div *= 10);
                }
            }
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
}