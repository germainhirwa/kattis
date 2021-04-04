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

        /*
        My goal here is to use UFDS. I will try to connect (union) all the lands and possibly the clouds together if adjacent
        In the end, my UFDS will have sets where each set's representative is either land, cloud or water.
        If it's water, discard it.
        If it's land, add 1 to the island count.
        However, if it's cloud, the set may contain land, which we have to add 1 to the island count. If the set has full of C's, then we can assume they are all water and hence don't add.

        I will use the hasLand boolean for unionSet to keep track whether the set contains land.
        To do this, the UFDS must have another boolean array "land" to store whether it is land or not.

        Example

        CCWWW -> CCL's will be in the same set. Since the set contains an L, this is counted as one island.
        LWWWC
        WWWCC -> The three C's will be in the same set. No L's here, so it's all water. Not an island.
        WWWWW
        LCCLL -> LCCLL will be in the same set. Since it contains an L, this is counted as one more island.
        */

        for (int i = 0; i < m; i++) {
            String row = sc.readLine();
            for (int j = 0; j < n; j++) {
                int k = row.charAt(j); // I use the ASCII value for easy comparation
                // ASCII of C is 67, L is 76
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
                // Check all representative whose set has land and is not water (it may be cloud)
                // First boolean : check if it is a representative/parent
                // Second boolean : check if the set has land
                // Third boolean : check if itself is not water (double-check)
                if (ufds.p[i*n+j] == i*n+j && ufds.land[i*n+j] && map[i][j] != 0)
                    count++;

                // Again, why second boolean check exists? Imagine a map with all clouds and waters but no land, the answer is 0
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
        else return p[i] = findSet(p[i]);
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

This is because when I go through (0,3) there is no neighbouring land but the representative is the C next to it.
I must do the or operation for both x and y in the unionSet method
*/