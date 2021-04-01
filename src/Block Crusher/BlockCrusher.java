// Using Reader class

import java.io.*;
import java.util.*;

public class BlockCrusher {
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

        public String readLine() throws IOException {
            byte[] buf = new byte[64]; // line length
            int cnt = 0, c;
            while ((c = read()) != -1) {
                if (c == '\n') {
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
            int r = sc.nextInt(), c = sc.nextInt();
            if (r == 0 && c == 0) {
                writer.flush();
                return;
            }
            int[][] blocks = new int[r][c]; // 2D array to store the strength of the blocks, we will determine the graph weight from here

            // Fill the 2D array
            for (int i = 0; i < r; i++) {
                String line = sc.readLine();
                for (int j = 0; j < c; j++)
                    blocks[i][j] = line.charAt(j)-48;
            }

            // Connecting each vertex denoting each block
            AdjacencyList graph = new AdjacencyList(r*c+2);
            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++) {
                    // Check neighbouring blocks and then connect them
                    if (i > 0) {
                        if (j > 0)
                            graph.connect(i*c+j,(i-1)*c+j-1,blocks[i-1][j-1]); // up left
                        if (j < c-1)
                            graph.connect(i*c+j,(i-1)*c+j+1,blocks[i-1][j+1]); // up right
                        graph.connect(i*c+j,(i-1)*c+j,blocks[i-1][j]); // up middle
                    }

                    if (i < r-1) {
                        if (j > 0)
                            graph.connect(i*c+j,(i+1)*c+j-1,blocks[i+1][j-1]); // down left
                        if (j < c-1)
                            graph.connect(i*c+j,(i+1)*c+j+1,blocks[i+1][j+1]); // down right
                        graph.connect(i*c+j,(i+1)*c+j,blocks[i+1][j]); // down middle
                    }

                    if (j > 0)
                        graph.connect(i*c+j,i*c+j-1,blocks[i][j-1]); // middle left
                    if (j < c-1)
                        graph.connect(i*c+j,i*c+j+1,blocks[i][j+1]); // middle right
                }
            }

            for (int i = 0; i < c; i++) {
                graph.connect(r*c,i,blocks[0][i]);
                graph.connect((r-1)*c+i,r*c+1,0);
            }

            Set<Integer> hs = graph.SSSPDijkstra(r*c,r*c+1);

            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++) {
                    if (hs.contains(i*c+j))
                        writer.print(" ");
                    else
                        writer.print(blocks[i][j]);
                }
                writer.println();
            }

            writer.println();
        }
    }
}

class AdjacencyList {
    public List<List<Pair>> list;
    public int numVertices;
    public int[] p;
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
        p = new int[numVertices]; // p too for predecessor
        for (int i = 0; i < numVertices; i++) {
            D[i] = Integer.MAX_VALUE;
            p[i] = -1;
        }
        D[s] = 0;
    }

    public void relax (int u, int v, int w) {
        if (D[u] != Integer.MAX_VALUE && D[v] > D[u] + w) { // if SP can be shortened
            D[v] = D[u] + w; // relax this edge
            p[v] = u; // remember/update the predecessor
        }
    }

    public Set<Integer> SSSPDijkstra (int s, int t) { // Modified Dijkstra's Algorithm
        initSSSP(s);

        Set<Integer> backtrack = new HashSet<Integer>();

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

        int curr = t;
        while (curr != -1) {
            backtrack.add(curr);
            curr = p[curr];
        }

        return backtrack; // [dest, p[dest], ..., source]
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