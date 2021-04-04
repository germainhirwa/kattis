// Using Reader class
import java.io.*;
import java.util.*;

public class MillionaireMadness2 {
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

        // We can solve this problem with a graph, specifically Adjacency List, then we will apply Prim's algorithm from the source
        // Then search a path from the MST to the end (possibly BFS/DFS)
        int r = sc.nextInt(), c = sc.nextInt();
        int[][] coins = new int[r][c]; // 2D array to store the height of the coins, we will determine the graph weight from here

        // Fill the 2D array
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++)
                coins[i][j] = sc.nextInt();

        // Connecting each vertex denoting each coin stack
        AdjacencyList graph = new AdjacencyList(r*c,coins);
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                // Check neighbouring stacks and then connect them
                if (j > 0)
                    graph.connect(i*c+j,i*c+(j-1),Math.max(0,coins[i][j-1]-coins[i][j])); // left
                if (j < c-1)
                    graph.connect(i*c+j,i*c+(j+1),Math.max(0,coins[i][j+1]-coins[i][j])); // right
                if (i > 0)
                    graph.connect(i*c+j,(i-1)*c+j,Math.max(0,coins[i-1][j]-coins[i][j])); // above
                if (i < r-1)
                    graph.connect(i*c+j,(i+1)*c+j,Math.max(0,coins[i+1][j]-coins[i][j])); // below
            }
        }

        writer.println(graph.MST(0,r*c-1)); // simply call the function
        writer.flush();
    }
}

class AdjacencyList { // D/W graph DS
    public List<List<Pair>> list;
    public int numVertices;
    public boolean[] taken;
    public int[] parent;
    public PriorityQueue<Triple> pq;
    public int coins[][];

    public AdjacencyList (int V, int[][] arr) {
        numVertices = V; // number of vertices
        coins = arr; // store the coin 2D array here for easy access
        list = new ArrayList<List<Pair>>(); // main adjacency list
        taken = new boolean[V]; // taken boolean array for MST method
        parent = new int[V]; // and a parent array to backtrack from destination after the MST path is formed
        
        for (int i = 0; i < V; i++) {
            list.add(new ArrayList<Pair>());
            taken[i] = false; // Initialize to false
            parent[i] = -1; // Initialize to -1
        }

        // Priority queue for MST, decided to make a queue of triples and not pairs so that I can convert to AL form easily, i.e. list of pairs
        PrimComparator pc = new PrimComparator();
        pq = new PriorityQueue<Triple>(pc);
    }

    public void connect (int a, int b, int w) { list.get(a).add(new Pair(b,w)); }

    // This will return the edges that create the MST
    // The format of each entry is <src, dest, weight>, just like the original Edge List
    public int MST (int s, int d) { // we will only run this once, hence initialization of taken boolean and parent int array is at the start of AL construction
        List<List<Pair>> mst = new ArrayList<List<Pair>>();
        int result = 0; // our final answer

        for (int i = 0; i < numVertices; i++)
            mst.add(new ArrayList<Pair>());

        // Source already taken part in MST
        taken[s] = true;
        for (Pair e : list.get(s)) // enqueue other edges connected to s
            pq.add(new Triple(s,e.dest,e.weight));

        while (!pq.isEmpty()) { // have some unprocessed edges
            Triple curr = pq.poll(); // edge with smallest weight
            if (!taken[curr.dest]) { // if that adjacent vertex is not taken yet
                mst.get(curr.source).add(new Pair(curr.dest,curr.weight)); // add that edge to MST
                parent[curr.dest] = curr.source; // set parent of that vertex
                taken[curr.dest] = true; // set that vertex as taken
                for (Pair e : list.get(curr.dest)) { // enqueue all the untaken adjacent edges to the PQ
                    if (!taken[e.dest])
                        pq.add(new Triple(curr.dest,e.dest,e.weight));
                }
            }
        }

        int temp = d; // start from destination
        while (temp != s) { // keep backtracking and...
            for (Pair e : mst.get(parent[temp])) {
                if (e.dest == temp) {
                    result = Math.max(result,e.weight); // keep track the maximum weight of the edges alongside the BFS path
                    break;
                }
            }
            temp = parent[temp];
        }

        return result;
    }
}

class Pair {
    public int dest; // destination
    public int weight; // weight

    public Pair (int v, int w) {
        dest = v;
        weight = w;
    }
}

class Triple {
    public int dest;
    public int weight;
    public int source; // source

    public Triple (int s, int v, int w) {
        source = s;
        dest = v;
        weight = w;
    }
}

class PrimComparator implements Comparator<Triple> { // for comparator of priority queue
    public int compare (Triple t1, Triple t2) {
        // priority : weight first, then the destination vertex, then source vertex
        if (t1.weight == t2.weight) {
            if (t1.dest == t2.dest)
                return t1.source - t2.source;
            else
                return t1.dest - t2.dest;
        } else
            return t1.weight - t2.weight;
    }
}