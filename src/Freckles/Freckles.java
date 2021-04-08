// Using Reader class
import java.io.*;
import java.util.*;

public class Freckles {
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

        public double nextDouble() throws IOException {
            double ret = 0, div = 1;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)
                c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
            if (c == '.') {
                while ((c = read()) >= '0' && c <= '9') {
                    ret += (c - '0') / (div *= 10);
                }
            }
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
        
        int t = sc.nextInt();
        while (t-- > 0) {
            int p = sc.nextInt();
            AdjacencyMatrix graph = new AdjacencyMatrix(p);
            double[][] points = new double[p][2];
            for (int i = 0; i < p; i++) {
                points[i][0] = sc.nextDouble();
                points[i][1] = sc.nextDouble();
            }
            for (int i = 0; i < p; i++) {
                for (int j = i+1; j < p; j++)
                    graph.connect(i,j,Math.hypot(points[i][0]-points[j][0],points[i][1]-points[j][1]));
            }

            writer.printf("%.2f\n",graph.MSTCost());
            writer.println();
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

            for (int j = 0; j < numVertices; j++) {
                if (!B[j] && A[j] > matrix[minIdx][j]) // if not taken and smaller weight, update array
                    A[j] = matrix[minIdx][j];
            }
        }
        
        return mst;
    }
}