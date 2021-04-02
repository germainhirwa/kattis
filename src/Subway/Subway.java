import java.io.*;
import java.util.*;

public class Subway {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        // Input source and target
        String[] line = sc.readLine().split(" ");
        int x1 = Integer.parseInt(line[0]);
        int y1 = Integer.parseInt(line[1]);
        int x2 = Integer.parseInt(line[2]);
        int y2 = Integer.parseInt(line[3]);
        
        int x = 0, y = 0, V = 0, lines = 0;
        List<List<Integer>> subwayX = new ArrayList<List<Integer>>();
        List<List<Integer>> subwayY = new ArrayList<List<Integer>>();
        List<Integer> stops = new ArrayList<Integer>();
        stops.add(0);
        try {
            while (true) {
                List<Integer> lineX = new ArrayList<Integer>();
                List<Integer> lineY = new ArrayList<Integer>();
                String[] subline = sc.readLine().split(" ");
                for (int i = 0; i < subline.length/2-1; i++) {
                    lineX.add(Integer.parseInt(subline[2*i]));
                    lineY.add(Integer.parseInt(subline[2*i+1]));
                    V++;
                }
                stops.add(V);
                subwayX.add(lineX);
                subwayY.add(lineY);
                lines++;
            }
        } catch (Exception e) {} // do nothing
        
        // Adjacency list
        // The weights will be the time taken from one point to another
        AdjacencyList graph = new AdjacencyList(V+2);

        // Connect two stops in the same line
        for (int i = 0; i < lines; i++) {
            for (int j = 0; j < subwayX.get(i).size()-1; j++) {
                for (int k = j+1; k < subwayX.get(i).size(); k++)
                    graph.connect(stops.get(i)+j, stops.get(i)+k, Math.hypot(subwayX.get(i).get(j)-subwayX.get(i).get(k),subwayY.get(i).get(j)-subwayY.get(i).get(k))/(k == j+1 ? 40 : 10));
            }
        }

        // Connect two stops from different lines
        for (int i = 0; i < lines; i++) {
            for (int j = i+1; j < lines; j++) {
                for (int k = 0; k < subwayX.get(i).size(); k++) {
                    for (int l = 0; l < subwayX.get(j).size(); l++)
                        graph.connect(stops.get(i)+k, stops.get(j)+l, Math.hypot(subwayX.get(i).get(k)-subwayX.get(j).get(l),subwayY.get(i).get(k)-subwayY.get(j).get(l))/10);
                }
            }
        }

        // Connect all stations to source and destination
        for (int i = 0; i < lines; i++) {
            for (int j = 0; j < subwayX.get(i).size(); j++) {
                graph.connect(V, stops.get(i)+j, Math.hypot(subwayX.get(i).get(j)-x1,subwayY.get(i).get(j)-y1)/10);
                graph.connect(V+1, stops.get(i)+j, Math.hypot(subwayX.get(i).get(j)-x2,subwayY.get(i).get(j)-y2)/10);
            }
        }

        // Connect source to destination
        graph.connect(V, V+1, Math.hypot(x1-x2,y1-y2)/10);

        // Run Dijkstra's algorithm to find the shortest time needed
        writer.println(Math.round(0.06*graph.SSSPDijkstra(V,V+1))); // index V is source, index V+1 is destination
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

    public void connect (int a, int b, double w) {
        list.get(a).add(new Pair(b,w));
        list.get(b).add(new Pair(a,w));
    }

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