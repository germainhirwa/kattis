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

        /*
        I will model the problem with a graph where the dominos are the vertices and the relations are the edges.
        Our goal is to find the number of vertices with no incoming edges, i.e. there is no other domino that knocks this domino.
        Then the DFS spanning tree from each vertex will cover all the vertices related to that each vertex.
        In other word, the DFS spanning tree from a vertex will tell you the dominos that will be knocked if the source domino is knocked.
        Using BFS instead of DFS is possible but will make the code longer as I will reuse DFS for the second traversal.

        This is similar to Kosaraju's algorithm, especially in the DFS toposort part.
        By doing DFS toposort, we have actually converted the graph into a DAG, as the initial graph may contain a cycle.
        After this, we have obtained a "topological ordering" of the graph.
        In other word, if we knock the dominos in that order, it will minimize the number of knocks.

        Now simply run DFS traversal again. This part is similar to UFDS but I decided to use the DFSRecursive method again.
        Start from the first vertex that is in the topological order (the output array will be in reverse so the rightmost vertex)
        For each new unvisited vertex that is met after a DFS recursive traversal, add the final answer by 1.
        */

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
    public boolean[] visited; // visited boolean array
    public List<Integer> toposort; // to store the topological ordering of the graph which is converted to DAG

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
                                                            // Added a boolean forToposort because we are going to run DFSRecursive for two different instances
                                                            // For toposort itself and for the next DFS traversal, which you shouldn't modify the toposort again
        visited[u] = true; // That vertex is now visited
        for (int i = 0; i < list.get(u).size(); i++) { // For all unvisited neighbours of u...
            if (!visited[list.get(u).get(i)]) // Do traversal recursively and update parent
                DFSRecursive(list.get(u).get(i),forToposort);
        }

        if (forToposort)
            toposort.add(u);
    }

    public int solve () { // Similar to Kosaraju's Algorithm to create the "SCCs" of the graph
        // DFS topological sort of G
        toposort(); // toposort will know be the array of the post-ordering proccesing of the vertices
                    // hence reversed

        // Initialize visited array
        visited = new boolean[numVertices];
        for (int i = 0; i < numVertices; i++)
            visited[i] = false;

        // Process vertices of toposort from right to left
        int ans = 0; // This will be our final answer
        for (int i = numVertices-1; i >= 0; i--) {
            if (!visited[toposort.get(i)]) {
                ans++;
                DFSRecursive(toposort.get(i),false);
            }
        }

        return ans;
    }
}