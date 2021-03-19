// Using Reader class

import java.io.*;
import java.util.*;

public class TenKinds2 {
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
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
            return ret;
        }

        public String readLine() throws IOException {
            byte[] buf = new byte[1024]; // line length
            int cnt = 0, c;
            while ((c = read()) != -1) {
                if (c == '\n') {
                    if (cnt != 0) {
                        break;
                    }
                    else {
                        continue;
                    }
                }
                buf[cnt++] = (byte)c;
            }
            return new String(buf, 0, cnt);
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

    public static int coordToIndex (int y, int x, int n) { // given an (m) x n array, find the index of (y,x)
        return y*n + x;
    }

    public static void main(String[] args) throws IOException {
        Reader sc = new Reader();
        PrintWriter writer = new PrintWriter(System.out);

        int m = sc.nextInt();
        int n = sc.nextInt();
        
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
                if (i == 0 && j == 0) { // corner top left, neighbours are (1,0) and (0,1) if exist
                    if (m > 1 && map[1][0] == map[i][j])
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(1,0,n));
                    if (n > 1 && map[0][1] == map[i][j])
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(0,1,n));
                } else if (i == 0 && j == n-1) { // corner top right, neighbours are (0,n-2) and (1,n-1) if exist
                    if (n > 1 && map[0][n-2] == map[i][j])
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(0,n-2,n));
                    if (m > 1 && map[1][n-1] == map[i][j])
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(1,n-1,n));
                } else if (i == m-1 && j == 0) { // corner bottom left, neighbours are (m-1,1) and (m-2,0) if exist
                    if (n > 1 && map[m-1][1] == map[i][j])
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(m-1,1,n));
                    if (m > 1 && map[m-2][0] == map[i][j])
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(m-2,0,n));
                } else if (i == m-1 && j == n-1) { // corner bottom right, neighbours are (m-2,n-1) and (m-1,n-2) if exist
                    if (m > 1 && map[m-2][n-1] == map[i][j])
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(m-2,n-1,n));
                    if (n > 1 && map[m-1][n-2] == map[i][j])
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(m-1,n-2,n));
                } else if (j == 0) { // left edge, neighbours are above, right, and below
                    if (map[i-1][0] == map[i][j])
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i-1,0,n));
                    if (map[i+1][0] == map[i][j])
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i+1,0,n));
                    if (n > 1 && map[i][1] == map[i][j])
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i,1,n));
                } else if (j == n-1) { // right edge, neighbours are above, left, and below
                    if (map[i-1][n-1] == map[i][j])
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i-1,n-1,n));
                    if (map[i+1][n-1] == map[i][j])
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i+1,n-1,n));
                    if (n > 1 && map[i][n-2] == map[i][j])
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i,n-2,n));
                } else if (i == 0) { // top edge, neighbours are left, right, and below
                    if (map[0][j-1] == map[i][j])
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(0,j-1,n));
                    if (map[0][j+1] == map[i][j])
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(0,j+1,n));
                    if (m > 1 && map[1][j] == map[i][j])
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(1,j,n));
                } else if (i == m-1) { // bottom edge, neighbours are above, left, and right
                    if (map[m-1][j-1] == map[i][j])
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(m-1,j-1,n));
                    if (map[m-1][j+1] == map[i][j])
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(m-1,j+1,n));
                    if (m > 1 && map[m-2][j] == map[i][j])
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(m-2,j,n));
                } else { // other than that, have 4 neighbours
                    if (map[i][j-1] == map[i][j])
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i,j-1,n));
                    if (map[i][j+1] == map[i][j])
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i,j+1,n));
                    if (map[i-1][j] == map[i][j])
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i-1,j,n));
                    if (map[i+1][j] == map[i][j])
                        ufds.unionSet(coordToIndex(i,j,n),coordToIndex(i+1,j,n));
                }
            }
        }

        // Number of queries
        int q = sc.nextInt();
        while (q-- > 0) {
            int r1 = sc.nextInt()-1;
            int c1 = sc.nextInt()-1;
            int r2 = sc.nextInt()-1;
            int c2 = sc.nextInt()-1;
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