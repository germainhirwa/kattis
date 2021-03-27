import java.io.*;
import java.util.*;

public class CountingStars {
    public static int coordToIndex (int y, int x, int n) { // given an (m) x n array, find the index of (y,x)
        return y*n + x;
    }

    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);

        int caseNo = 1;
        try {
            while (true) {
                String[] line = sc.readLine().split(" ");
                int m = Integer.parseInt(line[0]);
                int n = Integer.parseInt(line[1]);
                
                // Create a UFDS to store each point
                UnionFind ufds = new UnionFind(m*n);
                // And an array for the map representation
                int[][] map = new int[m][n];

                for (int i = 0; i < m; i++) {
                    String row = sc.readLine();
                    for (int j = 0; j < n; j++) {
                        int k = row.charAt(j);
                        map[i][j] = (k == 45 ? 1 : 0);
                    }
                }

                for (int i = 0; i < m; i++) {
                    for (int j = 0; j < n; j++) {
                        if (map[i][j] != 0) {
                            if (i == 0 && j == 0) { // corner top left, neighbours are (1,0) and (0,1) if exist
                                if (m > 1 && map[1][0] != 0)
                                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(1,0,n));
                                if (n > 1 && map[0][1] != 0)
                                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(0,1,n));
                            } else if (i == 0 && j == n-1) { // corner top right, neighbours are (0,n-2) and (1,n-1) if exist
                                if (n > 1 && map[0][n-2] != 0)
                                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(0,n-2,n));
                                if (m > 1 && map[1][n-1] != 0)
                                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(1,n-1,n));
                            } else if (i == m-1 && j == 0) { // corner bottom left, neighbours are (m-1,1) and (m-2,0) if exist
                                if (n > 1 && map[m-1][1] != 0)
                                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(m-1,1,n));
                                if (m > 1 && map[m-2][0] != 0)
                                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(m-2,0,n));
                            } else if (i == m-1 && j == n-1) { // corner bottom right, neighbours are (m-2,n-1) and (m-1,n-2) if exist
                                if (m > 1 && map[m-2][n-1] != 0)
                                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(m-2,n-1,n));
                                if (n > 1 && map[m-1][n-2] != 0)
                                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(m-1,n-2,n));
                            } else if (j == 0) { // left edge, neighbours are above, right, and below
                                if (map[i-1][0] != 0)
                                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i-1,0,n));
                                if (map[i+1][0] != 0)
                                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i+1,0,n));
                                if (n > 1 && map[i][1] != 0)
                                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i,1,n));
                            } else if (j == n-1) { // right edge, neighbours are above, left, and below
                                if (map[i-1][n-1] != 0)
                                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i-1,n-1,n));
                                if (map[i+1][n-1] != 0)
                                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i+1,n-1,n));
                                if (n > 1 && map[i][n-2] != 0)
                                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i,n-2,n));
                            } else if (i == 0) { // top edge, neighbours are left, right, and below
                                if (map[0][j-1] != 0)
                                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(0,j-1,n));
                                if (map[0][j+1] != 0)
                                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(0,j+1,n));
                                if (m > 1 && map[1][j] != 0)
                                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(1,j,n));
                            } else if (i == m-1) { // bottom edge, neighbours are above, left, and right
                                if (map[m-1][j-1] != 0)
                                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(m-1,j-1,n));
                                if (map[m-1][j+1] != 0)
                                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(m-1,j+1,n));
                                if (m > 1 && map[m-2][j] != 0)
                                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(m-2,j,n));
                            } else { // other than that, have 4 neighbours
                                if (map[i][j-1] != 0)
                                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i,j-1,n));
                                if (map[i][j+1] != 0)
                                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i,j+1,n));
                                if (map[i-1][j] != 0)
                                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i-1,j,n));
                                if (map[i+1][j] != 0)
                                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i+1,j,n));
                            }
                        }
                    }
                }

                int count = 0;
                for (int i = 0; i < m; i++) {
                    for (int j = 0; j < n; j++) {
                        if (ufds.p[i*n+j] == i*n+j && map[i][j] != 0)
                            count++;
                    }
                }

                writer.println("Case "+caseNo+": "+count);
                caseNo++;
            }
        } catch (Exception e) {
            writer.flush();
            return;
        }
    }
}

class UnionFind {
    public int[] p;
    public int[] rank;

    public UnionFind(int N) {
        p = new int[N];
        rank = new int[N];
        for (int i = 0; i < N; i++) {
            p[i] = i;
            rank[i] = 0;
        }
    }

    public int findSet(int i) { 
        if (p[i] == i) return i;
        else {
            p[i] = findSet(p[i]);
            return p[i]; 
        } 
    }

    public Boolean isSameSet(int i, int j) { return findSet(i) == findSet(j); }

    public void unionSet(int i, int j) {
        if (!isSameSet(i, j)) {
            int x = findSet(i), y = findSet(j);
            // rank is used to keep the tree short
            if (rank[x] > rank[y]) {
                p[y] = x;
            } else {
                p[x] = y;
                if (rank[x] == rank[y])
                    rank[y] = rank[y]+1;
            }
        }
    }
}