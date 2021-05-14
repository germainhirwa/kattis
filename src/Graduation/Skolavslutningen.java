// Using Reader class

import java.io.*;
import java.util.*;

public class Skolavslutningen {
    public static void main(String[] args) throws IOException {
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter writer = new PrintWriter(System.out);
        
        String[] line = sc.readLine().split(" ");
        int n = Integer.parseInt(line[0]);
        int m = Integer.parseInt(line[1]);
        int k = Integer.parseInt(line[2]);

        UFDS u = new UFDS(k+m);
        while (n-- > 0) {
            String row = sc.readLine();
            for (int i = 0; i < m; i++)
                u.unionSet(row.charAt(i)-65,k+i);
        }

        writer.println(u.nds);
        writer.flush();
    }
}

class UFDS {
    public int[] p;
    public int[] rank;
    public int nds;

    public UFDS(int N) {
        nds = N;
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
            nds--;
            if (rank[x] > rank[y])
                p[y] = x;
            else { 
                p[x] = y;
                if (rank[x] == rank[y])
                    rank[y]++;
            } 
        } 
    }
}