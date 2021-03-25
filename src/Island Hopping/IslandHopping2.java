// Uses EL, don't use the Reader class since it can't handle doubles well

import java.io.*;
import java.util.*;

public class IslandHopping2 {
    
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        int t = Integer.parseInt(sc.readLine());
        while (t-- > 0) {
            int m = Integer.parseInt(sc.readLine());
            double[][] points = new double[m][2];
            for (int i = 0; i < m; i++) {
                String[] line = sc.readLine().split(" ");
                points[i][0] = Double.parseDouble(line[0]);
                points[i][1] = Double.parseDouble(line[1]);
            }

            EdgeList el = new EdgeList(m);
            for (int i = 0; i < m; i++) {
                for (int j = i+1; j < m; j++) {
                    el.connect(i,j,Math.hypot(points[i][0]-points[j][0],points[i][1]-points[j][1]));
                }
            }

            writer.println(el.MSTCost());
        }

        writer.flush();
    }
}

class EdgeList {
    public List<Triple> list;
    public int numVertices;

    public EdgeList (int V) {
        numVertices = V;
        list = new ArrayList<Triple>();
    }

    public void connect (int a, int b, double w) {
        list.add(new Triple(Math.min(a,b),Math.max(a,b),w));
    }

    public double MSTCost () {
        UnionFind ufds = new UnionFind(numVertices);
        KruskalComparator kc = new KruskalComparator();
        list.sort(kc);
        double cost = 0;

        for (int i = 0; i < list.size(); i++) {
            if (!ufds.isSameSet(list.get(i).first,list.get(i).second)) {
                cost += list.get(i).third;
                ufds.unionSet(list.get(i).first,list.get(i).second);
            }
            if (ufds.numDisjointSets() == 1) { // all vertices inside MST
                break;
            }
        }

        return cost;
    }
}

class Triple {
    public int first;
    public int second;
    public double third;

    public Triple (int a, int b, double w) {
        first = a;
        second = b;
        third = w;
    }
}

class KruskalComparator implements Comparator<Triple> {
    public int compare (Triple t1, Triple t2) {
        if (t1.third == t2.third) {
            if (t1.first == t2.first)
                return t1.second - t2.second;
            else
                return t1.first - t1.first;
        } else
            return Double.compare(t1.third,t2.third);
    }
}

class UnionFind {
    public int[] p;
    public int[] rank;
    public int numSets;

    public UnionFind(int N) {
        p = new int[N];
        rank = new int[N];
        numSets = N;
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
            numSets--; 
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

    public int numDisjointSets() { return numSets; }
}