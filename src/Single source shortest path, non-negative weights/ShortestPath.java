// Using Reader class

import java.io.*;
import java.util.*;

public class ShortestPath {
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
            int n = sc.nextInt(), m = sc.nextInt(), q = sc.nextInt(), s = sc.nextInt();
            if (n == 0 && m == 0 && q == 0 && s == 0) {
                writer.flush();
                return;
            }

            AdjacencyList graph = new AdjacencyList(n);
            while (m-- > 0)
                graph.connect(sc.nextInt(),sc.nextInt(),sc.nextInt());
            
            graph.doDijkstra(s);

            while (q-- > 0) {
                int cost = graph.D[sc.nextInt()];
                writer.println(cost == Integer.MAX_VALUE ? "Impossible" : cost);
            }

            writer.println();
        }
    }
}

class AdjacencyList {
    public List<List<Pair>> list;
    public int numVertices;
    public int[] D;

    public AdjacencyList (int V) {
        numVertices = V;
        list = new ArrayList<List<Pair>>();
        for (int i = 0; i < V; i++)
            list.add(new ArrayList<Pair>());
    }

    public void connect (int a, int b, int w) { list.get(a).add(new Pair(b,w)); }

    public void initSSSP (int s) {
        D = new int[numVertices]; // Initialize the D array
        for (int i = 0; i < numVertices; i++)
            D[i] = Integer.MAX_VALUE;
        D[s] = 0;
    }

    public void relax (int u, int v, int w) {
        if (D[u] != Integer.MAX_VALUE && D[v] > D[u] + w) // if SP can be shortened
            D[v] = D[u] + w; // relax this edge
    }

    public void doDijkstra (int s) { // Modified Dijkstra's Algorithm
        initSSSP(s);

        List<Integer> backtrack = new ArrayList<Integer>();

        DijkstraComparator dc = new DijkstraComparator();
        PriorityQueue<Pair> pq = new PriorityQueue<Pair>(dc);
        pq.offer(new Pair(s,0)); // recall my version of Pair is (dest, weight) not (weight, dest)

        while (!pq.isEmpty()) {
            Pair ud = pq.poll(); // pair (u,d)
            if (ud.second == D[ud.first]) { // important check, lazy DS
                for (Pair e : list.get(ud.first)) {
                    if (D[e.first] > D[ud.first] + e.second) { // can relax
                        relax(ud.first, e.first, e.second); // relax
                        pq.offer(new Pair(e.first,D[e.first]));
                    }
                }
            }
        }
    }
}

class Pair {
    public int first; // represents the destination
    public int second; // represents the weight

    public Pair (int v, int w) {
        first = v;
        second = w;
    }
}

class DijkstraComparator implements Comparator<Pair> {
    public int compare (Pair p1, Pair p2) {
        if (p1.second == p2.second)
            return p1.first - p2.first;
        else
            return p1.second - p2.second;
    }
}