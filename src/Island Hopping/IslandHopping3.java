// Uses AL, also slightly slower than using AM, don't use the Reader class since it can't handle doubles well in this case

import java.io.*;
import java.util.*;

public class IslandHopping3 {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int t = Integer.parseInt(sc.readLine());
        while (t-- > 0) {
            int m = Integer.parseInt(sc.readLine());
            double[][] points = new double[m][2];
            for (int i = 0; i < m; i++) {
                String[] line = sc.readLine().split(" ");
                points[i][0] = Double.parseDouble(line[0]);
                points[i][1] = Double.parseDouble(line[1]);
            }

            AdjacencyList al = new AdjacencyList(m);
            for (int i = 0; i < m; i++) {
                for (int j = i+1; j < m; j++) {
                    al.connect(i,j,Math.hypot(points[i][0]-points[j][0],points[i][1]-points[j][1]));
                }
            }

            writer.println(al.MSTCost());
        }

        writer.flush();
    }
}

class AdjacencyList {
    public List<List<Pair>> list;
    public int numVertices;

    public AdjacencyList (int V) {
        numVertices = V;
        list = new ArrayList<List<Pair>>();
        for (int i = 0; i < V; i++) {
            list.add(new ArrayList<Pair>());
        }
    }

    public void connect (int a, int b, double w) { // weighted graph
        list.get(a).add(new Pair(b,w));
        list.get(b).add(new Pair(a,w));
    }

    public double MSTCost () { // O(V^2)
        double inf = Double.MAX_VALUE;
        double mst = 0;
        int vCount = 0;
        double[] A = new double[numVertices]; // smallest weight array
        boolean[] B = new boolean[numVertices]; // taken boolean array
        for (int i = 0; i < numVertices; i++) {
            A[i] = inf;
            B[i] = false;
        }
        A[0] = 0; // my Pair remains (v, w) not (w, v)

        while (vCount != numVertices) {
            // Find v where A[v] is minimum in A
            int minIdx = 0;
            double minVal = A[0];
            for (int i = 1; i < numVertices; i++) {
                if (A[i] < minVal) {
                    minIdx = i;
                    minVal = A[i];
                }
            }
            mst += minVal;
            vCount++;

            // v already added to MST
            B[minIdx] = true;
            A[minIdx] = inf;

            for (Pair e : list.get(minIdx)) {
                if (!B[e.first] && A[e.first] > e.second) // if not taken and smaller weight, update array
                    A[e.first] = e.second;
            }
        }
        
        return mst;
    }
}

class Pair {
    // This is how we access the elements of the pair, just like in C++
    public int first;
    public double second;

    public Pair (int v, double w) {
        first = v;
        second = w;
    }
}