// The term 'other drawer' refers to the drawers in A's and B's set only, not a stack

import java.io.*;
import java.util.*;

public class Ladice {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        String[] line = sc.readLine().split(" ");
        int N = Integer.parseInt(line[0]);
        int L = Integer.parseInt(line[1]);
        UnionFind ufds = new UnionFind(L);
        while (N-- > 0) {
            String[] line2 = sc.readLine().split(" ");
            int A = Integer.parseInt(line2[0])-1;
            int B = Integer.parseInt(line2[1])-1;
            ufds.unionSet(A,B);

            // The 2 first rules are equivalent considering the UFDS algorithm, and so are the 2 last rules
            int parentA = ufds.findSet(A);
            if (ufds.fill[parentA] != 0) {
                ufds.fill[parentA]--;
                writer.println("LADICA");
            } else {
                writer.println("SMECE");
            }
            /*
            writer.println(A+" "+B);
            writer.println(Arrays.toString(ufds.p));
            */
        }

        writer.flush();
    }
}

class UnionFind {
    public int[] p;
    public int[] rank;
    public int numSets;
    public int[] fill; // number of items in itself and nodes below it

    public UnionFind(int N) {
        p = new int[N];
        rank = new int[N];
        fill = new int[N];
        numSets = N;
        for (int i = 0; i < N; i++) {
            p[i] = i;
            rank[i] = 0;
            fill[i] = 1;
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
            numSets--; 
            int x = findSet(i), y = findSet(j);
            if (rank[x] > rank[y]) {
            	p[y] = x;
                fill[x] += fill[y];
            } else { 
            	p[x] = y;
                if (rank[x] == rank[y]) {
                    rank[y] = rank[y]++;
                    fill[y] += fill[x];
                }
            } 
        } 
    }
}