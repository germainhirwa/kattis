import java.io.*;
import java.util.*;

public class Fire2 {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int t = Integer.parseInt(sc.readLine());
        while (t-- > 0) {
            String[] rc = sc.readLine().split(" ");
            int c = Integer.parseInt(rc[0]);
            int r = Integer.parseInt(rc[1]);

            int[][] maze = new int[r][c];

            int s = 0;
            List<Integer> fires = new ArrayList<Integer>();
            for (int i = 0; i < r; i++) {
                String row = sc.readLine();
                for (int j = 0; j < c; j++) {
                    if (row.charAt(j) == '#')
                        maze[i][j] = 0;
                    else {
                        maze[i][j] = 1;
                        if (row.charAt(j) == '@')
                            s = i*c+j;
                        else if (row.charAt(j) == '*')
                            fires.add(i*c+j);
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

            graph.doBFS(s); // fill the Y@ array
            graph.doBFS(fires); // fill the F* array

            boolean possible = false;
            int minTime = Integer.MAX_VALUE;
            for (int i = 0; i < c; i++) {
                if (graph.Y[i] < Integer.MAX_VALUE && graph.Y[i] < graph.F[i]) { // top row
                    minTime = Math.min(minTime, graph.Y[i]);
                    possible = true;
                }
                if (graph.Y[(r-1)*c+i] != Integer.MAX_VALUE && graph.Y[(r-1)*c+i] < graph.F[(r-1)*c+i]) { // bottom row
                    minTime = Math.min(minTime, graph.Y[(r-1)*c+i]);
                    possible = true;
                }
            }

            for (int i = 0; i < r; i++) {
                if (graph.Y[i*c] != Integer.MAX_VALUE && graph.Y[i*c] < graph.F[i*c]) { // left column
                    minTime = Math.min(minTime, graph.Y[i*c]);
                    possible = true;
                }
                if (graph.Y[i*c+(c-1)] != Integer.MAX_VALUE && graph.Y[i*c+(c-1)] < graph.F[i*c+(c-1)]) { // right column
                    minTime = Math.min(minTime, graph.Y[i*c+(c-1)]);
                    possible = true;
                }
            }

            if (possible)
                writer.println(minTime+1); // extra one step to officially exit the maze
            else
                writer.println("IMPOSSIBLE");
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
            Y[i] = Integer.MAX_VALUE;
            F[i] = Integer.MAX_VALUE;
        }
    }

    public void connect (int a, int b) { list.get(a).add(b); }

    public void doBFS (int s) {
        Y[s] = 0;

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
                    Y[list.get(u).get(i)] = Y[u] + 1;
                    q.offer(list.get(u).get(i));
                }
            }
        }
    }

    public void doBFS (List<Integer> fires) {
        Queue<Integer> q = new LinkedList<Integer>();
        visited = new boolean[numVertices];
        for (int i = 0; i < numVertices; i++)
            visited[i] = false;

        for (int f : fires) {
            F[f] = 0;
            visited[f] = true;
            q.offer(f);
        }

        while (!q.isEmpty()) {
            Integer u = q.poll();
            for (int i = 0; i < list.get(u).size(); i++) {
                if (!visited[list.get(u).get(i)]) {
                    visited[list.get(u).get(i)] = true;
                    F[list.get(u).get(i)] = F[u] + 1;
                    q.offer(list.get(u).get(i));
                }
            }
        }
    }
}