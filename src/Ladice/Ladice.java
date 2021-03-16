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

        // Create a UFDS with L elements (L sets initially)
        UnionFind ufds = new UnionFind(L);
        while (N-- > 0) {
            String[] line2 = sc.readLine().split(" ");
            int A = Integer.parseInt(line2[0])-1;
            int B = Integer.parseInt(line2[1])-1;

            // Union the A-th drawer and the B-th drawer in the UFDS
            ufds.unionSet(A,B);

            // The 2 first rules are equivalent considering the UFDS algorithm, and same for the 2 last rules they are equivalent in this case
            int parentA = ufds.findSet(A);
            if (ufds.fill[parentA] != 0) { // we still have a slot!
                ufds.fill[parentA]--;
                writer.println("LADICA");
            } else { // no slot, throw
                writer.println("SMECE");
            }
        }

        writer.flush();
    }
}

class UnionFind {
    public int[] p;
    public int[] rank;
    public int numSets;
    public int[] fill; // number of items in the set containing itself (will take the representatives only)

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
                fill[x] += fill[y]; // add fill to the representative
            } else { 
                p[x] = y;
                if (rank[x] == rank[y]) {
                    rank[y] = rank[y]++;
                    fill[y] += fill[x]; // add fill to the representative
                }
            } 
        } 
    }
}