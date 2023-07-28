// Using Reader class

import java.io.*;
import java.util.*;

public class ShortestPath3 {
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

        long INF = 1000000000000L;

        while (true) {
            int n = sc.nextInt(), m = sc.nextInt(), q = sc.nextInt(), s = sc.nextInt();
            if (n == 0 && m == 0 && q == 0 && s == 0) {
                writer.flush();
                return;
            }

            Graph graph = new Graph(n);
            while (m-- > 0)
                graph.connect(sc.nextInt(),sc.nextInt(),sc.nextInt());
            
            graph.doSSSP(s);

            while (q-- > 0) {
                int t = sc.nextInt();
                long sp = graph.D[t];
                if (sp == INF)
                    writer.println("Impossible");
                else if (graph.neg[t])
                    writer.println("-Infinity");
                else
                    writer.println(sp);
            }

            writer.println();
        }
    }
}

class Graph {
    public List<Triple> list;
    public int numVertices;
    public long[] D;
    public boolean[] neg;
    public long INF = 1000000000000L;

    public Graph (int V) {
        numVertices = V;
        list = new ArrayList<Triple>();
    }

    public void connect (int a, int b, int w) { list.add(new Triple(a,b,w)); }

    public void relax (int u, int v, int w) {
        if (D[u] != INF && D[v] > D[u] + w) // if SP can be shortened
            D[v] = D[u] + w; // relax this edge
    }

    public void doSSSP (int s) {
        // Initialize
        D = new long[numVertices];
        neg = new boolean[numVertices];
        for (int i = 0; i < numVertices; i++) {
            D[i] = INF;
            neg[i] = false;
        }
        D[s] = 0;

        // Bellman-Ford's algorithm
        for (int i = 0; i < numVertices-1; i++)
            for (Triple edge : list)
                relax(edge.first, edge.second, edge.third);

        // Negative cycle check
        boolean stillFound = true;
        while (stillFound) {
            stillFound = false;
            for (Triple edge : list) {
                if (D[edge.first] != INF && D[edge.second] > D[edge.first] + edge.third && !neg[edge.second]) {
                    D[edge.second] = -INF; // don't use Long.MAX_VALUE nor Integer.MAX_VALUE
                    neg[edge.second] = true;
                    stillFound = true;
                }
            }
        }
    }
}

class Triple {
    public int first;
    public int second;
    public int third;

    public Triple (int a, int b, int w) {
        first = a;
        second = b;
        third = w;
    }
}