import java.io.*;
import java.util.*;

public class Amoebas {
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
        boolean[][] map = new boolean[m][n];

        for (int i = 0; i < m; i++) {
            String row = sc.readLine();
            for (int j = 0; j < n; j++) {
                int k = row.charAt(j); // I use the ASCII value for easy comparation
                map[i][j] = k == 35;
            }
        }

        int[] dirr = {-1,-1,-1,0,0,1,1,1};
        int[] dirc = {-1,0,1,-1,1,-1,0,1};

        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (map[i][j])
                    for (int p = 0; p < 8; p++)
                        if (0 <= i+dirr[p] && i+dirr[p] <= m-1 && 0 <= j+dirc[p] && j+dirc[p] <= n-1 && map[i+dirr[p]][j+dirc[p]])
                            ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i+dirr[p],j+dirc[p],n));

        int count = 0;
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (ufds.p[i*n+j] == i*n+j && map[i][j])
                    count++;

        writer.println(count);
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
        else return p[i] = findSet(p[i]);
    }

    public boolean isSameSet(int i, int j) { return findSet(i) == findSet(j); }

    public void unionSet(int i, int j) {
        if (!isSameSet(i, j)) {
            int x = findSet(i), y = findSet(j);
            // rank is used to keep the tree short
            if (rank[x] > rank[y]) {
                p[y] = x;
            } else {
                p[x] = y;
                if (rank[x] == rank[y])
                    rank[y]++;
            }
        }
    }
}