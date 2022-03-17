import java.io.*;
import java.util.*;

class AdjacencyList {
    public List<List<Pair>> list;
    public int numVertices;
    public boolean directed;

    public AdjacencyList (int V, boolean dir) {
        directed = dir;
        numVertices = V;
        list = new ArrayList<List<Pair>>();
        for (int i = 0; i < V; i++)
            list.add(new ArrayList<Pair>());
    }

    public void connect (int a, int b) { // unweighted graph
        connect(a,b,1);
    }

    public void connect (int a, int b, int w) { // weighted graph
        if (a != b) {
            list.get(a).add(new Pair(b,w));
            if (!directed)
                list.get(b).add(new Pair(a,w));
        }
    }

    public boolean DFS (int s) { // DFS from a single source
        return helper(s, new HashSet<Integer>());
    }
    
    public boolean helper(int s, Set<Integer> set) {
        if (set.contains(s))
            return true;
        set.add(s);
        for (int i = 0; i < list.get(s).size(); i++) {
            if (helper(list.get(s).get(i).first, set))
                return true;
        }
        set.remove(s);
        return false;
    }
}

class Pair implements Comparable<Pair> {
    // This is how we access the elements of the pair, just like in C++
    public int first;
    public int second;

    public Pair (int v, int w) {
        first = v;
        second = w;
    }

    @Override
    public int compareTo (Pair other) {
        if (this.first != other.first)
            return this.first - other.first;
        else
            return this.second - other.second;
    }
}

public class RunningMoM {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter writer = new PrintWriter(System.out);

        int n = Integer.parseInt(br.readLine());
        Map<String, Integer> hm = new HashMap<String, Integer>();
        AdjacencyList al = new AdjacencyList(2 * n, true);
        while (n-- > 0) {
            String[] line = br.readLine().split(" ");
            if (hm.get(line[0]) == null)
                hm.put(line[0], hm.size());
            if (hm.get(line[1]) == null)
                hm.put(line[1], hm.size());
            al.connect(hm.get(line[0]), hm.get(line[1]));
        }

        while (true) {
            String city = br.readLine();
            if (city == null) {
                writer.flush();
                return;
            }
            writer.print(city);
            writer.print(" ");
            writer.println(hm.get(city) == null ? "trapped" : (al.DFS(hm.get(city)) ? "safe" : "trapped"));
        }
    }
}