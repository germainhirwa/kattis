// Using Reader class
import java.io.*;
import java.util.*;

public class Cats {
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
            int m = sc.nextInt();
            int c = sc.nextInt();
            AdjacencyList al = new AdjacencyList(c);
            for (int i = 0; i < c*(c-1)/2; i++) {
                al.connect(sc.nextInt(),sc.nextInt(),sc.nextInt());
            }
            writer.println(al.MSTCost() <= m-c ? "yes" : "no");
        }

        writer.flush();
    }
}

class AdjacencyList {
    public List<List<Pair>> list;
    public int numVertices;

    public AdjacencyList (int V) {
        numVertices = V;
        list = new ArrayList<List<Pair>>();
        for (int i = 0; i < V; i++) {
            list.add(new ArrayList<Pair>());
        }
    }

    public void connect (int a, int b, int w) { // weighted graph
        list.get(a).add(new Pair(b,w));
        list.get(b).add(new Pair(a,w));
    }

    public int MSTCost () { // O(V^2)
        int inf = Integer.MAX_VALUE;
        int mst = 0;
        int vCount = 0;
        int[] A = new int[numVertices]; // smallest weight array
        boolean[] B = new boolean[numVertices]; // taken boolean array
        for (int i = 0; i < numVertices; i++) {
            A[i] = inf;
            B[i] = false;
        }
        A[0] = 0; // my Pair remains (v, w) not (w, v)

        while (vCount != numVertices) {
            // Find v where A[v] is minimum in A
            int minIdx = 0;
            int minVal = A[0];
            for (int i = 1; i < numVertices; i++) {
                if (A[i] < minVal) {
                    minIdx = i;
                    minVal = A[i];
                }
            }
            mst += minVal;
            vCount++;

            // v already added to MST
            B[minIdx] = true;
            A[minIdx] = inf;

            for (Pair e : list.get(minIdx)) {
                if (!B[e.first] && A[e.first] > e.second) // if not taken and smaller weight, update array
                    A[e.first] = e.second;
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