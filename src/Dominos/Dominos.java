// Using Reader class
import java.io.*;
import java.util.*;

public class Dominos {
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

        // The whole problem revolves around counting "strongly connected components" in a graph (SCC)
        // Actually we're just using the Kosaraju's algorithm but we're not transposing the graph
        /*
            The key here is to convert the graph into a DAG, since the graph may contain a cycle
            It turns out that Kosaraju's Algorithm can do this after doing topological sort
            Any unvisited vertex before the next DFS traversal must have no incoming edge, i.e. the domino we should knock
        */
        // I will use Adjacency List to represent the graph

        int t = sc.nextInt(); // number of test cases
        while (t-- > 0) {
            int V = sc.nextInt(), E = sc.nextInt(); // number of vertices and edges
            AdjacencyList graph = new AdjacencyList(V); // create the graph DS
            
            while (E-- > 0)
                graph.connect(sc.nextInt()-1, sc.nextInt()-1); // connect the edges

            writer.println(graph.solve()); // solve and print the answer
        }

        writer.flush();
    }
}

class AdjacencyList { // D/U graph DS
    public List<List<Integer>> list;
    public int numVertices;
    public boolean[] visited;
    public List<Integer> toposort;

    public AdjacencyList (int V) {
        numVertices = V; // number of vertices
        list = new ArrayList<List<Integer>>(); // main adjacency list, list of integers instead of pairs since it is an unweighted graph
        for (int i = 0; i < V; i++)
            list.add(new ArrayList<Integer>());
    }

    public void connect (int a, int b) { list.get(a).add(b); } // simply add b to list.get(a)

    public void toposort () { // DFS toposort, the toposort attribute will now be the reversed order of the result
        // Initialization
        visited = new boolean[numVertices];
        for (int i = 0; i < numVertices; i++)
            visited[i] = false; // Initialize to false

        toposort = new ArrayList<Integer>();

        for (int i = 0; i < numVertices; i++) {
            if (!visited[i])
                DFSRecursive(i,true);
        }
    }

    public void DFSRecursive (int u, boolean forToposort) { // Recursive DFS traversal
        visited[u] = true; // That vertex is now visited
        for (int i = 0; i < list.get(u).size(); i++) { // For all unvisited neighbours of u...
            if (!visited[list.get(u).get(i)]) { // Do traversal recursively and update parent
                DFSRecursive(list.get(u).get(i),forToposort);
            }
        }

        if (forToposort)
            toposort.add(u);
    }

    public int solve () { // Kosaraju's Algorithm to create the "SCCs" of the graph
        // DFS topological sort of G
        toposort(); // toposort will know be the array of the post-ordering proccesing of the vertices

        // Initialize visited
        visited = new boolean[numVertices];
        for (int i = 0; i < numVertices; i++)
            visited[i] = false;

        // Process vertices of toposort from right to left
        int ans = 0;
        for (int i = numVertices-1; i >= 0; i--) {
            if (!visited[toposort.get(i)]) {
                ans++;
                DFSRecursive(toposort.get(i),false);
            }
        }

        return ans;
    }
}