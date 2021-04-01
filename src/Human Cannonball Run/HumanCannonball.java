import java.io.*;
import java.util.*;

public class HumanCannonball {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        // Input source and target
        String[] a = sc.readLine().split(" ");
        String[] b = sc.readLine().split(" ");
        double x1 = Double.parseDouble(a[0]);
        double x2 = Double.parseDouble(b[0]);
        double y1 = Double.parseDouble(a[1]);
        double y2 = Double.parseDouble(b[1]);
        
        // Number of cannons
        int V = Integer.parseInt(sc.readLine());
        double[] X = new double[V]; // to store all the x-coordinates of the cannons
        double[] Y = new double[V]; // to store all the y-coordinates of the cannons
        
        // Adjacency list
        // The weights will be the time taken from one point to another
        AdjacencyList graph = new AdjacencyList(V+2);

        // Input all the cannons' coordinates
        for (int i = 0; i < V; i++) {
            String[] line = sc.readLine().split(" ");
            X[i] = Double.parseDouble(line[0]);
            Y[i] = Double.parseDouble(line[1]);
        }

        // Connect each two cannons first
        double dist;
        for (int i = 0; i < V; i++) {
            for (int j = i+1; j < V; j++) {
                dist = Math.hypot(X[j]-X[i],Y[j]-Y[i]);
                // 2 seconds to launch you with the cannon
                // Assume the distance is dist, then walk |dist-50| meters to the next cannon
                // This takes extra |dist-50|/5 seconds
                graph.connect(i,j,2+Math.abs(dist-50)/5); // time taken from cannon i to reach cannon j
                graph.connect(j,i,2+Math.abs(dist-50)/5); // time taken from cannon j to reach cannon i
            }
        }

        // Connect source and destination with a cannon
        for (int i = 0; i < V; i++) {
            graph.connect(V,i,Math.hypot(x1-X[i],y1-Y[i])/5); // walk from source to cannon i
            graph.connect(i,V+1,2+Math.abs(Math.hypot(x2-X[i],y2-Y[i])-50)/5); // 2 seconds to launch from cannon i, walk to destination
        }

        // Finally connect source and destination (in case must walk the whole way through)
        graph.connect(V,V+1,Math.hypot(x2-x1,y2-y1)/5);

        // Run Dijkstra's algorithm to find the shortest time needed
        writer.println(graph.SSSPDijkstra(V,V+1)); // index V is source, index V+1 is destination
        writer.flush();
    }
}

class AdjacencyList {
    public List<List<Pair>> list;
    public int numVertices;
    public double[] D;

    public AdjacencyList (int V) {
        numVertices = V;
        list = new ArrayList<List<Pair>>();
        for (int i = 0; i < V; i++) {
            list.add(new ArrayList<Pair>());
        }
    }

    public void connect (int a, int b, double w) { list.get(a).add(new Pair(b,w)); }

    public void initSSSP (int s) {
        D = new double[numVertices]; // Initialize the D array
        for (int i = 0; i < numVertices; i++)
            D[i] = Double.MAX_VALUE;
        D[s] = 0;
    }

    public void relax (int u, int v, double w) {
        if (D[u] != Double.MAX_VALUE && D[v] > D[u] + w) // if SP can be shortened
            D[v] = D[u] + w; // relax this edge
    }

    public double SSSPDijkstra (int s, int t) { // Modified Dijkstra's Algorithm
        initSSSP(s);

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

        return D[t];
    }
}

class Pair {
    public int first; // represents the destination
    public double second; // represents the weight

    public Pair (int v, double w) {
        first = v;
        second = w;
    }
}

class DijkstraComparator implements Comparator<Pair> {
    public int compare (Pair p1, Pair p2) {
        if (p1.second == p2.second)
            return p1.first - p2.first;
        else
            return Double.compare(p1.second, p2.second);
    }
}