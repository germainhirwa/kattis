// Uses AM, don't use the Reader class since it can't handle doubles well in this case

import java.io.*;
import java.util.*;

public class IslandHopping {
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

            AdjacencyMatrix am = new AdjacencyMatrix(m);
            for (int i = 0; i < m; i++) {
                for (int j = i+1; j < m; j++) {
                    am.connect(i,j,Math.hypot(points[i][0]-points[j][0],points[i][1]-points[j][1]));
                }
            }

            writer.println(am.MSTCost());
        }

        writer.flush();
    }
}

class AdjacencyMatrix {
    public double[][] matrix;
    public int numVertices;

    public AdjacencyMatrix (int V) {
        numVertices = V;
        matrix = new double[V][V];
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++)
                matrix[i][j] = 0;
        }
    }

    public void connect (int a, int b, double w) { // weighted graph
        matrix[a][b] = w;
        matrix[b][a] = w;
    }

    public double MSTCost () {
        double inf = Integer.MAX_VALUE;
        double mst = 0;
        int vCount = 0;
        double[] A = new double[numVertices]; // smallest weight array
        boolean[] B = new boolean[numVertices]; // taken boolean array
        for (int i = 0; i < numVertices; i++) {
            A[i] = inf;
            B[i] = false;
        }
        A[0] = 0; // set source to 0

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

            for (int i = 0; i < numVertices; i++) { // traverse the minIdx-th row of the AM
                if (!B[i])
                    A[i] = Math.min(A[i],matrix[minIdx][i]);
            }
        }
        
        return mst;
    }
}