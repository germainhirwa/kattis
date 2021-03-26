// Using Reader class
import java.io.*;
import java.util.*;

public class Hyacinth {
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
        
        int n = sc.nextInt();
        if (n == 2)
            writer.println("1 2\n1 2");
        else {
            AdjacencyList al = new AdjacencyList(n);
            n--;
            while (n-- > 0) {
                al.connect(sc.nextInt()-1,sc.nextInt()-1);
            }

            al.assign();
            for (int i = 0; i < al.numVertices; i++)
                writer.println(al.hyacinth[i][0]+" "+al.hyacinth[i][1]);
        }
        writer.flush();
    }
}

class AdjacencyList {
    public List<List<Pair>> list;
    public int numVertices;
    public int numVisited;
    public boolean[] visited;
    public int[][] hyacinth;

    public AdjacencyList (int V) {
        numVertices = V;
        hyacinth = new int[V][2];
        list = new ArrayList<List<Pair>>();
        for (int i = 0; i < V; i++) {
            list.add(new ArrayList<Pair>());
            hyacinth[i][0] = 0;
            hyacinth[i][1] = 0;
        }
    }

    public void connect (int a, int b) {
        list.get(a).add(new Pair(b,0));
        list.get(b).add(new Pair(a,0));
    }

    public void assign () {
        int curr = 0; // start from vertex 0
        int nextNum = 1; // next assignee will get number 1
        int edgesAssigned = 0; // number of assigned edges
        Queue<Integer> q = new LinkedList<Integer>();
        q.offer(0);

        while (edgesAssigned != numVertices-1) {
            curr = q.poll();
            Collections.sort(list.get(curr)); // sort by decreasing weight
            // we want a sequence of A-0-0-...-0 or A-B-B-...-B or 0-0-...-0
            List<Pair> neighbors = list.get(curr);
            if (neighbors.get(0).second == 0) { // 0-0-...-0 case
                neighbors.get(0).second = nextNum;
                // Must update from the neighbor's side too
                for (Pair e : list.get(neighbors.get(0).first)) {
                    if (e.first == curr)
                        e.second = nextNum;
                }
                edgesAssigned++;
                nextNum++;
                q.offer(neighbors.get(0).first);

                for (int i = 1; i < neighbors.size(); i++) {
                    neighbors.get(i).second = nextNum;
                    for (Pair e : list.get(neighbors.get(i).first)) {
                        if (e.first == curr)
                            e.second = nextNum;
                        q.offer(neighbors.get(i).first);
                    }
                    edgesAssigned++;
                }

                if (neighbors.size() != 1)
                    nextNum++;
            } else {
                if (neighbors.size() > 1 && neighbors.get(1).second == 0) { // A-0-0-...-0 case
                    for (int i = 1; i < neighbors.size(); i++) {
                        neighbors.get(i).second = nextNum;
                        for (Pair e : list.get(neighbors.get(i).first)) {
                            if (e.first == curr)
                                e.second = nextNum;
                            q.offer(neighbors.get(i).first);
                        }
                        edgesAssigned++;
                    }
                    nextNum++;
                }
                // else, A-B-B-...-B case, do nothing
            }
            Collections.sort(list.get(curr));
        }

        for (int i = 0; i < numVertices; i++) {
            for (Pair e : list.get(i)) {
                if (hyacinth[i][0] == 0)
                    hyacinth[i][0] = e.second;
                else if (hyacinth[i][1] == 0 && hyacinth[i][0] != e.second)
                    hyacinth[i][1] = e.second;
            }
        }

        for (int i = 0; i < numVertices; i++) {
            if (hyacinth[i][1] == 0) {
                hyacinth[i][1] = nextNum;
                nextNum++;
            }
        }
    }
}

class Pair implements Comparable<Pair> {
    public int first, second;

    public Pair (int f, int s) {
        first = f;
        second = s;
    }

    @Override
    public int compareTo (Pair o) {
        return o.second - this.second; // to be sorted by number assigned in decreasing order
    }
}