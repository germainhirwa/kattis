import java.io.*;
import java.util.*;

public class RaidTeams {
    public static void main(String[] args) throws IOException {
        FastIO fio = new FastIO();
        int t = fio.nextInt();
        TreeMap<Integer, TreeSet<String>> tm1 = new TreeMap<Integer, TreeSet<String>>();
        TreeMap<Integer, TreeSet<String>> tm2 = new TreeMap<Integer, TreeSet<String>>();
        TreeMap<Integer, TreeSet<String>> tm3 = new TreeMap<Integer, TreeSet<String>>();
        HashMap<String, Integer> th1 = new HashMap<String, Integer>();
        HashMap<String, Integer> th2 = new HashMap<String, Integer>();
        HashMap<String, Integer> th3 = new HashMap<String, Integer>();

        int m = t / 3;
        while (t-- > 0) {
            String name = fio.next();
            int s1 = fio.nextInt(), s2 = fio.nextInt(), s3 = fio.nextInt();
            if (tm1.get(s1) == null)
                tm1.put(s1, new TreeSet<String>());
            if (tm2.get(s2) == null)
                tm2.put(s2, new TreeSet<String>());
            if (tm3.get(s3) == null)
                tm3.put(s3, new TreeSet<String>());
            tm1.get(s1).add(name);
            tm2.get(s2).add(name);
            tm3.get(s3).add(name);
            th1.put(name, s1);
            th2.put(name, s2);
            th3.put(name, s3);
        }

        while (m-- > 0) {
            String[] team = new String[3];
            
            int hi1 = tm1.lastEntry().getKey();
            team[0] = tm1.get(hi1).pollFirst();
            tm2.get(th2.get(team[0])).remove(team[0]);
            tm3.get(th3.get(team[0])).remove(team[0]);
            if (tm1.get(hi1).isEmpty())
                tm1.remove(hi1);
            if (tm2.get(th2.get(team[0])).isEmpty())
                tm2.remove(th2.get(team[0]));
            if (tm3.get(th3.get(team[0])).isEmpty())
                tm3.remove(th3.get(team[0]));

            int hi2 = tm2.lastEntry().getKey();
            team[1] = tm2.get(hi2).pollFirst();
            tm1.get(th1.get(team[1])).remove(team[1]);
            tm3.get(th3.get(team[1])).remove(team[1]);
            if (tm2.get(hi2).isEmpty())
                tm2.remove(hi2);
            if (tm1.get(th1.get(team[1])).isEmpty())
                tm1.remove(th1.get(team[1]));
            if (tm3.get(th3.get(team[1])).isEmpty())
                tm3.remove(th3.get(team[1]));

            int hi3 = tm3.lastEntry().getKey();
            team[2] = tm3.get(hi3).pollFirst();
            tm2.get(th2.get(team[2])).remove(team[2]);
            tm1.get(th1.get(team[2])).remove(team[2]);
            if (tm3.get(hi3).isEmpty())
                tm3.remove(hi3);
            if (tm2.get(th2.get(team[2])).isEmpty())
                tm2.remove(th2.get(team[2]));
            if (tm1.get(th1.get(team[2])).isEmpty())
                tm1.remove(th1.get(team[2]));

            Arrays.sort(team);
            fio.print(team[0]);
            fio.print(" ");
            fio.print(team[1]);
            fio.print(" ");
            fio.println(team[2]);
        }

        fio.close();
    }
}

class FastIO extends PrintWriter { 
    BufferedReader br; 
    StringTokenizer st;

    public FastIO() { 
        super(new BufferedOutputStream(System.out)); 
        br = new BufferedReader(new InputStreamReader(System.in));
    } 

    String next() { 
        while (st == null || ! st.hasMoreElements()) { 
            try { st = new StringTokenizer(br.readLine()); } 
            catch (IOException  e) { e.printStackTrace(); } 
        } 
        return st.nextToken(); 
    } 

    int nextInt() { return Integer.parseInt(next()); } 
    long nextLong() { return Long.parseLong(next()); } 
    double nextDouble() { return Double.parseDouble(next()); } 

    String nextLine() { 
        String str = ""; 
        try { str = br.readLine(); } 
        catch (IOException e) { e.printStackTrace(); } 
        return str; 
    } 
}