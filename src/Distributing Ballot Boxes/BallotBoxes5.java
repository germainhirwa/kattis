import java.io.*;
import java.util.*;

public class BallotBoxes5 {
    public static void main(String[] args) throws IOException {
        FastIO fio = new FastIO();
        
        while (true) {
            int N = fio.nextInt();

            if (N == -1) { // EOF
                fio.close();
                return;
            }

            int B = fio.nextInt();

            List<Integer> cities = new ArrayList<Integer>();
            int maxPop = 0, minPop = 1, midPop;
            for (int i = 0; i < N; i++) {
                int k = fio.nextInt();
                cities.add(k);
                maxPop = Math.max(k,maxPop);
            }

            while (minPop < maxPop) {
                midPop = (maxPop+minPop)/2;

                int boxes = 0;
                for (int i = 0; i < N; i++) {
                    boxes += (cities.get(i)+midPop-1)/midPop;
                }

                if (boxes > B) {
                    minPop = midPop+1;
                } else {
                    maxPop = midPop;
                }
            }

            fio.println(minPop);
        }
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