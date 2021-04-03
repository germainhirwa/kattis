// Using Reader class

import java.io.*;
import java.util.*;
public class FloweryTrails {
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
        
        int V = sc.nextInt(), E = sc.nextInt();
        AdjacencyList graph = new AdjacencyList(V);

        while (E-- > 0) {
            int u = sc.nextInt(), v = sc.nextInt(), w = sc.nextInt();
            if (u != v)
                graph.connect(u,v,w);
        }

        graph.SSSPDijkstra(0,V-1); // do Dijkstra's and modify D array

        int ans = 0;
        boolean visited[] = new boolean[V];
        for (int i = 0; i < V; i++)
            visited[i] = false;
        
        Queue<Integer> q = new LinkedList<Integer>();
        q.offer(V-1);
        while (!q.isEmpty()) {
            int c = q.poll();
            if (!visited[c]) {
                visited[c] = true;
                for (Pair e : graph.p.get(c)) {
                    q.offer(e.first);
                    ans += e.second*graph.lm.get(c).get(e.first).second;
                }
            }
        }

        writer.println(ans*2);
        writer.flush();
    }
}

class AdjacencyList {
    public List<List<Pair>> list;
    public int numVertices;
    public List<Set<Pair>> p;
    public int[] D;
    public List<Map<Integer,Pair>> lm;

    public AdjacencyList (int V) {
        numVertices = V;
        list = new ArrayList<List<Pair>>();
        lm = new ArrayList<Map<Integer,Pair>>(); // the value is (weight, count) in this case
                                                 // the key is the destination vertices

        for (int i = 0; i < V; i++) {
            list.add(new ArrayList<Pair>());
            lm.add(new HashMap<Integer,Pair>());
        }
    }

    public void connect (int a, int b, int w) {
        if (lm.get(a).get(b) == null) {
            lm.get(a).put(b, new Pair(w,1));
            lm.get(b).put(a, new Pair(w,1));
        } else if (lm.get(a).get(b).first == w) {
            lm.get(a).get(b).second++;
            lm.get(b).get(a).second++;
        } else if (lm.get(a).get(b).first > w) {
            lm.get(a).put(b, new Pair(w,1));
            lm.get(b).put(a, new Pair(w,1));
        }
    }

    public void initSSSP (int s) {
        // Finalize the connect method
        D = new int[numVertices]; // Initialize the D array
        p = new ArrayList<Set<Pair>>(); // p too for predecessor
        for (int i = 0; i < numVertices; i++) {
            D[i] = Integer.MAX_VALUE-1000;
            p.add(new HashSet<Pair>());
            for (int j : lm.get(i).keySet())
                list.get(i).add(new Pair(j,lm.get(i).get(j).first));
        }
        D[s] = 0;
    }

    public void relax (int u, int v, int w) {
        if (D[u] != Integer.MAX_VALUE-1000 && D[v] >= D[u] + w) { // if SP can be shortened
            if (D[v] > D[u] + w)
                p.get(v).clear();
            
            p.get(v).add(new Pair(u,w)); // remember/update the predecessor
            D[v] = D[u] + w; // relax this edge
        }
    }

    public void SSSPDijkstra (int s, int t) { // Modified Dijkstra's Algorithm
        initSSSP(s);

        DijkstraComparator dc = new DijkstraComparator();
        PriorityQueue<Pair> pq = new PriorityQueue<Pair>(dc);
        pq.offer(new Pair(s,0)); // recall my version of Pair is (dest, weight) not (weight, dest)

        while (!pq.isEmpty()) {
            Pair ud = pq.poll(); // pair (u,d)
            if (ud.second == D[ud.first]) { // important check, lazy DS
                for (Pair e : list.get(ud.first)) {
                    if (D[e.first] >= D[ud.first] + e.second) { // can relax
                        relax(ud.first, e.first, e.second); // relax
                        pq.offer(new Pair(e.first,D[e.first]));
                    }
                }
            }
        }
    }
}

class Pair {
    public int first; // represents the destination
    public int second; // represents the weight

    public Pair (int v, int w) {
        first = v;
        second = w;
    }

    @Override
    public int hashCode () { return first*10000+second; }

    @Override
    public boolean equals (Object obj) { return this.hashCode() == obj.hashCode(); }
}

class DijkstraComparator implements Comparator<Pair> {
    public int compare (Pair p1, Pair p2) {
        if (p1.second == p2.second)
            return p1.first - p2.first;
        else
            return p1.second - p2.second;
    }
}

/*
4 10
0 1 1
0 1 1
0 2 1
0 2 1
0 3 999
1 2 1
1 3 1
1 3 1
2 3 1
2 3 1

Output: 16
*/