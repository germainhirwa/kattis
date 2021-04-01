import java.io.*;
import java.util.*;

public class TenKinds {
    public static int coordToIndex (int y, int x, int n) { // given an (m) x n array, find the index of (y,x)
        return y*n + x;
    }

    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);

        String[] line = sc.readLine().split(" ");
        int m = Integer.parseInt(line[0]);
        int n = Integer.parseInt(line[1]);
        
        // Create a UFDS to store each point
        UnionFind ufds = new UnionFind(m*n);
        // And an array for the map representation
        int[][] map = new int[m][n];

        // Changing the input into the map array, nothing else
        for (int i = 0; i < m; i++) {
            String row = sc.readLine();
            for (int j = 0; j < n; j++) {
                int k = row.charAt(j);
                map[i][j] = (k == 48 ? 0 : 1);
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // Check for every point, if the neighbour is the same as them, union both
                if (j > 0 && map[i][j-1] == map[i][j])
                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i,j-1,n));
                if (j < n-1 && map[i][j+1] == map[i][j])
                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i,j+1,n));
                if (i > 0 && map[i-1][j] == map[i][j])
                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i-1,j,n));
                if (i < m-1 && map[i+1][j] == map[i][j])
                    ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i+1,j,n));
            }
        }

        // Number of queries
        int q = Integer.parseInt(sc.readLine());
        while (q-- > 0) {
            String[] line2 = sc.readLine().split(" ");
            int r1 = Integer.parseInt(line2[0])-1;
            int c1 = Integer.parseInt(line2[1])-1;
            int r2 = Integer.parseInt(line2[2])-1;
            int c2 = Integer.parseInt(line2[3])-1;
            // Check if (r1,c1) and (r2,c2) is contained in the same set/island, then check whether it's the binary "island" or the decimal "island"
            writer.println(ufds.isSameSet(coordToIndex(r1,c1,n),coordToIndex(r2,c2,n)) ? (map[r1][c1] == 1 ? "decimal" : "binary") : "neither");
        }
        writer.flush();
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
            if (rank[x] > rank[y])
                p[y] = x;
            else {
                p[x] = y;
                if (rank[x] == rank[y])
                    rank[y] = rank[y]+1;
            }
        }
    }
}