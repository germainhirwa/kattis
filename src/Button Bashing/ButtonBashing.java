// Using Reader class
import java.io.*;
import java.util.*;

public class ButtonBashing {
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
        
        int m = sc.nextInt();
        while (m-- > 0) {
            int n = sc.nextInt(), t = sc.nextInt();
            int[] d = new int[n];
            for (int i = 0; i < n; i++)
                d[i] = sc.nextInt();

            AdjacencyList graph = new AdjacencyList(3601);
            for (int i = 0; i < 3601; i++)
                for(int j = 0; j < n; j++)
                    if (i+d[j] <= 3600 && i+d[j] >= 0)
                        graph.connect(i,i+d[j]);
                    else if (i+d[j] < 0)
                        graph.connect(i,0);
                    else
                        graph.connect(i,3600);

            graph.doBFS(0);

            for (int i = t; i <= 3600; i++)
                if (graph.D[i] != Integer.MAX_VALUE) {
                    writer.print(graph.D[i]);
                    writer.print(" ");
                    writer.println(i-t);
                    break;
                }
        }

        writer.flush();
    }
}

class AdjacencyList {
    public List<List<Integer>> list;
    public int numVertices;
    public int[] D;
    public boolean[] visited;

    public AdjacencyList (int V) {
        numVertices = V;
        D = new int[V];
        list = new ArrayList<List<Integer>>();
        for (int i = 0; i < V; i++) {
            list.add(new ArrayList<Integer>());
            D[i] = Integer.MAX_VALUE;
        }
    }

    public void connect (int a, int b) { list.get(a).add(b); }

    public void doBFS (int s) {
        D[s] = 0;

        visited = new boolean[numVertices];
        for (int i = 0; i < numVertices; i++)
            visited[i] = false;

        Queue<Integer> q = new LinkedList<Integer>();
        q.offer(s);
        visited[s] = true;

        while (!q.isEmpty()) {
            Integer u = q.poll();
            for (int i = 0; i < list.get(u).size(); i++) {
                if (!visited[list.get(u).get(i)]) {
                    visited[list.get(u).get(i)] = true;
                    D[list.get(u).get(i)] = D[u] + 1;
                    q.offer(list.get(u).get(i));
                }
            }
        }
    }
}