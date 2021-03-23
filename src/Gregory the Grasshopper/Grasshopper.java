import java.io.*;
import java.util.*;

public class Grasshopper {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        while (true) {
            try {
                String[] line = sc.readLine().split(" ");
                int r = Integer.parseInt(line[0]);
                int c = Integer.parseInt(line[1]);
                int gr = Integer.parseInt(line[2])-1;
                int gc = Integer.parseInt(line[3])-1;
                int lr = Integer.parseInt(line[4])-1;
                int lc = Integer.parseInt(line[5])-1;
                if (r == 1 || c == 1)
                    writer.println((gr == lr && gc == lc) ? 0 : "impossible");
                else {
                    AdjacencyList al = new AdjacencyList(r,c);
                    int pl = al.shortestPathLength(gr*c+gc,lr*c+lc);

                    if (pl == -1)
                        writer.println("impossible");
                    else
                        writer.println(pl);
                }
            } catch (Exception e) {
                writer.flush();
                return;
            }
        }
    }
}

class AdjacencyList { // not so adjacency list, I removed the list for efficiency since we only do 1x BFS
    public int numVertices;
    public int[] depth;
    public int cols;

    public AdjacencyList (int r, int c) {
        numVertices = r*c;
        cols = c;
    }

    void BFS (int s, int t) { // BFS from a single source
        depth = new int[numVertices];
        int rows = numVertices/cols;
        for (int i = 0; i < numVertices; i++) {
            depth[i] = -1; // Initialize to -1
        }

        int[] q = new int[10000]; // Queue<Integer> is much slower than the primitive array
        int front = 0, back = 1;
        q[0] = s;
        depth[s] = 0;

        int[] temp;

        while (front != back) {
            Integer u = q[front];
            front++;

            int i = u/cols;
            int j = u % cols;
            temp = new int[8];
            for (int k = 0; k < 8; k++)
                temp[k] = -1;

            if (i-1 >= 0 && j-2 >= 0)
                temp[0] = ((i-1)*cols+(j-2));
            if (i-2 >= 0 && j-1 >= 0)
                temp[1] = ((i-2)*cols+(j-1));
            if (i-1 >= 0 && j+2 < cols)
                temp[2] = ((i-1)*cols+(j+2));
            if (i-2 >= 0 && j+1 < cols)
                temp[3] = ((i-2)*cols+(j+1));
            if (i+1 < rows && j-2 >= 0)
                temp[4] = ((i+1)*cols+(j-2));
            if (i+2 < rows && j-1 >= 0)
                temp[5] = ((i+2)*cols+(j-1));
            if (i+1 < rows && j+2 < cols)
                temp[6] = ((i+1)*cols+(j+2));
            if (i+2 < rows && j+1 < cols)
                temp[7] = ((i+2)*cols+(j+1));

            for (int v : temp) { // at most 8
                if (v != -1 && depth[v] == -1) {
                    depth[v] = depth[u] + 1;
                    if (v == t)
                        return;
                    q[back] = v;
                    back++;
                }
            }
        }
    }

    public int shortestPathLength (int u, int v) {
        BFS(u,v);
        return depth[v];
    }
}