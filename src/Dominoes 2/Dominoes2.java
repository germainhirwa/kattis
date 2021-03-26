// Using Reader class
import java.io.*;
import java.util.*;

public class Dominoes2 {
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
            int n = sc.nextInt(), m = sc.nextInt(), l = sc.nextInt();
            AdjacencyList al = new AdjacencyList(n);
            while (m-- > 0)
                al.connect(sc.nextInt()-1,sc.nextInt()-1);
            while (l-- > 0)
                al.DFS(sc.nextInt()-1);

            writer.println(al.numVisited);
        }

        writer.flush();
    }
}

class AdjacencyList {
    public List<List<Integer>> list;
    public int numVertices;
    public int numVisited;
    public boolean[] visited;

    public AdjacencyList (int V) {
        numVertices = V;
        numVisited = 0;
        list = new ArrayList<List<Integer>>();
        visited = new boolean[numVertices];
        for (int i = 0; i < V; i++) {
            list.add(new ArrayList<Integer>());
            visited[i] = false;
        }
    }

    public void connect (int a, int b) {
        list.get(a).add(b);
    }

    public void DFS (int u) {
        if (!visited[u]) {
            visited[u] = true;
            numVisited++;
            for (int i = 0; i < list.get(u).size(); i++)
                DFS(list.get(u).get(i));
        }
    }
}