import java.io.*;
import java.util.*;

public class Islands {
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

        for (int i = 0; i < m; i++) {
            String row = sc.readLine();
            for (int j = 0; j < n; j++) {
                int k = row.charAt(j); // I use the ASCII value for easy comparation
                map[i][j] = (k == 67 ? -1 : (k == 76 ? 1 : 0)); // -1 if cloud, 1 if land, 0 if water
                ufds.land[i*n+j] = (k == 76); // if there is land, initiate the land boolean to true for unionSet later
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // Check for every point that is not water
                if (map[i][j] != 0) {
                    // The union set takes two integers and a boolean to check whether one of the unioned numbers is land
                    if (j > 0 && map[i][j-1] != 0)
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i,j-1,n),map[i][j-1] == 1); // left
                    if (j < n-1 && map[i][j+1] != 0)
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i,j+1,n),map[i][j+1] == 1); // right
                    if (i > 0 && map[i-1][j] != 0)
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i-1,j,n),map[i-1][j] == 1); // above
                    if (i < m-1 && map[i+1][j] != 0)
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i+1,j,n),map[i+1][j] == 1); // below
                }
            }
        }

        int count = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // Check all representative whose set has land and is not water
                // First boolean : check if it is a representative/parent
                // Second boolean : check if the set has land
                // Third boolean : check if itself is not water (double-check)
                if (ufds.p[i*n+j] == i*n+j && ufds.land[i*n+j] && map[i][j] != 0)
                    count++;

                // Why second boolean check exists? Imagine a map with all clouds and waters but no land, the answer is 0
            }
        }

        writer.println(count);
        writer.flush();
    }
}

class UnionFind {
    public int[] p;
    public int[] rank;
    public boolean[] land; // to store whether the set has a single block of land or not

    public UnionFind(int N) {
        p = new int[N];
        rank = new int[N];
        land = new boolean[N];
        for (int i = 0; i < N; i++) {
            p[i] = i;
            rank[i] = 0;
            land[i] = false;
        }
    }

    public int findSet(int i) { 
        if (p[i] == i) return i;
        else {
            p[i] = findSet(p[i]);
            return p[i]; 
        } 
    }

    public boolean isSameSet(int i, int j) { return findSet(i) == findSet(j); }

    public void unionSet(int i, int j, boolean hasLand) {
        if (!isSameSet(i, j)) {
            int x = findSet(i), y = findSet(j);
            // rank is used to keep the tree short
            if (rank[x] > rank[y]) {
                p[y] = x;
                land[x] = land[x] || land[y] || hasLand; // representative must check if one of them is true, not just itself
            } else {
                p[x] = y;
                land[y] = land[x] || land[y] || hasLand; // representative must check if one of them is true, not just itself
                if (rank[x] == rank[y])
                    rank[y] = rank[y]+1;
            }
        }
    }
}

/*
My own test case which got me
4 4
LWLC
WLWC
LWLC
CCCC

This is because when I go through (0,3) no land neighbour but the representative is the next C.
I must do or for both x and y in unionSet
*/