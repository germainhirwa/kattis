// Using Reader class
import java.io.*;
import java.util.*;

public class NatureReserve {
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
        
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt(), m = sc.nextInt(), l = sc.nextInt(), s = sc.nextInt();
            AdjacencyList al = new AdjacencyList(n);
            int[] srcs = new int[s];
            for (int i = 0; i < s; i++)
                srcs[i] = sc.nextInt()-1;
            for (int i = 0; i < m; i++)
                al.connect(sc.nextInt()-1,sc.nextInt()-1,sc.nextInt()+l);
            int res = 0;
            writer.println(al.MSTCost(srcs));
        }

        writer.flush();
    }
}

class AdjacencyList {
    public List<List<Pair>> list;
    public int numVertices;
    public boolean[] taken;
    public PriorityQueue<Pair> pq;

    public AdjacencyList (int V) {
        numVertices = V;
        list = new ArrayList<List<Pair>>();
        for (int i = 0; i < V; i++) {
            list.add(new ArrayList<Pair>());
        }
        taken = new boolean[numVertices];
        for (int i = 0; i < numVertices; i++)
            taken[i] = false;
        PrimComparator pc = new PrimComparator();
        pq = new PriorityQueue<Pair>(pc);
    }

    public void connect (int a, int b, int w) { // weighted graph
        list.get(a).add(new Pair(b,w));
        list.get(b).add(new Pair(a,w));
    }

    public long MSTCost (int[] srcs) {
        long mst = 0;

        for (int s : srcs) {
            taken[s] = true;
            for (Pair e : list.get(s)) // enqueue other edges connected to s
                pq.add(e);
        }

        while (!pq.isEmpty()) { // have some unprocessed edges
            Pair curr = pq.poll();
            if (!taken[curr.first]) {
                mst += curr.second;
                taken[curr.first] = true;
                for (Pair e : list.get(curr.first)) {
                    if (!taken[e.first])
                        pq.add(e);
                }
            }
        }

        return mst;
    }
}

class Pair {
    public int first;
    public int second;

    public Pair (int v, int w) {
        first = v;
        second = w;
    }
}

class PrimComparator implements Comparator<Pair> {
    public int compare (Pair p1, Pair p2) {
        if (p1.second == p2.second)
            return p1.first - p2.first;
        else
            return p1.second - p2.second;
    }
}