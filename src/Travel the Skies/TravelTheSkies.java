// Using Reader class
import java.io.*;
import java.util.*;

public class TravelTheSkies {
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
    
    public static void main(String[] args) throws IOException {
        Reader sc = new Reader();
        PrintWriter writer = new PrintWriter(System.out);
        
        int k = sc.nextInt(), n = sc.nextInt(), m = sc.nextInt();
        // k = number of airports
        // n = number of days
        // m = number of flights

        int[] flights = new int[n]; // to store the number of flights in each day
        int[][] airportFill = new int[n][k]; // array of current fill in the airports
        AdjacencyList[] simulation = new AdjacencyList[n];
        for (int i = 0; i < n; i++) {
            simulation[i] = new AdjacencyList(k);
            flights[i] = 0;
        }

        for (int i = 0; i < m; i++) {
            int u = sc.nextInt(), v = sc.nextInt(), d = sc.nextInt(), z = sc.nextInt();
            // u_i = flight's starting location
            // v_i = flight's ending destination
            // d = the day of the flight
            // z = capacity of the flight
            simulation[d-1].connect(u-1,v-1,z);
            flights[d-1]++;
        }
        for (int j = 0; j < k*n; j++) {
            int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt();
            // a_j = airport index, 1 <= a_j <= k
            // b_j = the day for this specific input, 1 <= b_j <= n
            // c_j = number of customers in that airport on that day
            airportFill[b-1][a-1] = c;
        }

        int currDay = 1;
        while (currDay <= n) {
            AdjacencyList al = simulation[currDay-1];

            for (int f = 0; f < flights[currDay-1]; f++) {
                boolean foundFlight = false;
                // Check all the edges
                for (int i = 0; i < k && !foundFlight; i++) {
                    for (int j = 0; j < al.list.get(i).size() && !foundFlight; j++) {
                        if (!al.executed.get(i).get(j) && al.list.get(i).get(j).second <= airportFill[currDay-1][i]) {
                            al.executed.get(i).set(j,true);
                            airportFill[currDay-1][i] -= al.list.get(i).get(j).second;
                            if (currDay < n)
                                airportFill[currDay][al.list.get(i).get(j).first] += al.list.get(i).get(j).second;
                            foundFlight = true;
                        }
                    }
                }

                if (!foundFlight) {
                    writer.println("suboptimal");
                    writer.flush();
                    return;
                }
            }

            // Transfer all remaining passengers to next day
            if (currDay < n) {
                for (int i = 0; i < k; i++)
                    airportFill[currDay][i] += airportFill[currDay-1][i];
            }

            currDay++;
        }

        writer.println("optimal");
        writer.flush();
    }
}

class AdjacencyList { // directed, weighted graph
    public List<List<Pair>> list;
    public int numVertices;
    public List<List<Boolean>> executed;

    public AdjacencyList (int V) {
        numVertices = V;
        list = new ArrayList<List<Pair>>();
        executed = new ArrayList<List<Boolean>>();
        for (int i = 0; i < V; i++) {
            list.add(new ArrayList<Pair>());
            executed.add(new ArrayList<Boolean>());
        }
    }

    public void connect (int a, int b, int w) {
        list.get(a).add(new Pair(b,w));
        executed.get(a).add(false);
    }

    public String toString() { return list.toString(); }
}

class Pair {
    public int first;
    public int second;

    public Pair (int v, int w) {
        first = v;
        second = w;
    }

    public String toString () { return "<"+first+","+second+">"; }
}