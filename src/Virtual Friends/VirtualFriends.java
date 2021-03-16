import java.io.*;
import java.util.*;

public class VirtualFriends {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int t = Integer.parseInt(sc.readLine());
        while (t-- > 0) {
            int f = Integer.parseInt(sc.readLine());
            int curr = 0;
            UnionFind ufds = new UnionFind(2*f);
            Map<String,Integer> hm = new HashMap<String,Integer>();
            while (f-- > 0) {
                String[] line = sc.readLine().split(" ");
                String f1 = line[0], f2 = line[1];
                if (hm.get(f1) == null) {
                    hm.put(f1,curr);
                    curr++;
                }
                if (hm.get(f2) == null) {
                    hm.put(f2,curr);
                    curr++;
                }
                ufds.unionSet(hm.get(f1),hm.get(f2));
                writer.println(ufds.setSize(hm.get(f1)));
            }
        }

        writer.flush();
    }
}

class UnionFind {
    public int[] p;
    public int[] rank;
    public int[] size;

    public UnionFind(int N) {
        p = new int[N];
        rank = new int[N];
        size = new int[N];
        for (int i = 0; i < N; i++) {
            p[i] = i;
            rank[i] = 0;
            size[i] = 1;
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
                size[x] += size[y];
            } else { 
                p[x] = y;
                size[y] += size[x];
                if (rank[x] == rank[y]) 
                    rank[y] = rank[y]+1; 
            } 
        } 
    }

    public int setSize(int i) {
        return size[findSet(i)];
    }
}