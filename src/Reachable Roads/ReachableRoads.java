// Using Reader class
import java.io.*;
import java.util.*;

public class ReachableRoads {
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
            int v = sc.nextInt(), e = sc.nextInt();
            AdjacencyList al = new AdjacencyList(v);
            while (e-- > 0)
                al.connect(sc.nextInt(),sc.nextInt());
            writer.println(al.countCC()-1);
        }
        
        writer.flush();
    }
}

class AdjacencyList {
    public List<List<Integer>> list;
    public int numVertices;
    public boolean[] visited;

    public AdjacencyList (int V) {
        numVertices = V; // number of vertices
        list = new ArrayList<List<Integer>>(); // main adjacency list
        for (int i = 0; i < V; i++) {
            list.add(new ArrayList<Integer>());
        }
    }

    public void connect (int a, int b) {
        list.get(a).add(b);
        list.get(b).add(a);
    }

    public void DFSRecursive (int u) {
        visited[u] = true;
        for (int i = 0; i < list.get(u).size(); i++) {
            if (!visited[list.get(u).get(i)])
                DFSRecursive(list.get(u).get(i));
        }
    }

    public int countCC () { // connected components
        int ans = 0;

        visited = new boolean[numVertices];

        for (int i = 0; i < numVertices; i++) {
            visited[i] = false; // Initialize to 0
        }

        for (int i = 0; i < numVertices; i++) {
            if (!visited[i]) {
                ans++;
                DFSRecursive(i);
            }
        }

        return ans;
    }
}