import java.io.*;
import java.util.*;

// Taken from Fire2.java
public class Slikar {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        String[] rc = sc.readLine().split(" ");
        int r = Integer.parseInt(rc[0]);
        int c = Integer.parseInt(rc[1]);

        int[][] maze = new int[r][c];

        int s = 0;
        List<Integer> players = new ArrayList<Integer>();
        List<Integer> fires = new ArrayList<Integer>();
        for (int i = 0; i < r; i++) {
            String row = sc.readLine();
            for (int j = 0; j < c; j++) {
                if (row.charAt(j) == 'X')
                    maze[i][j] = 0;
                else {
                    maze[i][j] = 1;
                    if (row.charAt(j) == 'S')
                        players.add(i*c+j);
                    else if (row.charAt(j) == '*')
                        fires.add(i*c+j);
                    else if (row.charAt(j) == 'D')
                        s = i*c+j;
                }
            }
        }

        AdjacencyList graph = new AdjacencyList(r*c);
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (maze[i][j] == 1) {
                    if (i > 0 && maze[i-1][j] == 1)
                        graph.connect(i*c+j,(i-1)*c+j); // up
                    if (i < r-1 && maze[i+1][j] == 1)
                        graph.connect(i*c+j,(i+1)*c+j); // down
                    if (j > 0 && maze[i][j-1] == 1)
                        graph.connect(i*c+j,i*c+j-1); // left
                    if (j < c-1 && maze[i][j+1] == 1)
                        graph.connect(i*c+j,i*c+j+1); // right
                }
            }
        }

        graph.doBFS(fires, false, s);
        graph.doBFS(players, true, s);

        //writer.println(Arrays.toString(graph.Y) + " " + Arrays.toString(graph.F));
        if (graph.Y[s] != Integer.MIN_VALUE) {
            writer.println(graph.Y[s]);
        } else {
            writer.println("KAKTUS");
        }
        writer.flush();
    }
}

class AdjacencyList {
    public List<List<Integer>> list;
    public int numVertices;
    public int[] Y; // for You
    public int[] F; // for fire
    public boolean[] visited;

    public AdjacencyList (int V) {
        numVertices = V;
        list = new ArrayList<List<Integer>>();
        for (int i = 0; i < V; i++)
            list.add(new ArrayList<Integer>());
        Y = new int[numVertices]; // Initialize the Y array
        F = new int[numVertices]; // Initialize the F array
        for (int i = 0; i < numVertices; i++) {
            Y[i] = Integer.MIN_VALUE;
            F[i] = Integer.MIN_VALUE;
        }
    }

    public void connect (int a, int b) { list.get(a).add(b); }

    public void doBFS (List<Integer> pts, boolean info, int s) {
        int[] T = info ? this.Y : this.F;
        Queue<Integer> q = new LinkedList<Integer>();
        visited = new boolean[numVertices];
        for (int i = 0; i < numVertices; i++)
            visited[i] = false;

        for (int f : pts) {
            T[f] = 0;
            visited[f] = true;
            q.offer(f);
        }

        while (!q.isEmpty()) {
            Integer u = q.poll();
            if (info && this.Y[u] >= this.F[u] && this.F[u] != Integer.MIN_VALUE)
                continue;
            for (int i = 0; i < list.get(u).size(); i++) {
                if (!visited[list.get(u).get(i)]) {
                    visited[list.get(u).get(i)] = true;
                    if (!info && list.get(u).get(i) == s)
                        continue;
                    T[list.get(u).get(i)] = T[u] + 1;
                    q.offer(list.get(u).get(i));
                }
            }
        }
    }
}