// Using Reader class

import java.io.*;
import java.util.*;

public class KattissQuest2 {
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

        public String readWord() throws IOException {
            byte[] buf = new byte[64]; // line length
            int cnt = 0, c;
            while ((c = read()) != -1) {
                if (c == '\n' || c == ' ') {
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
        
        // This is a map of energy and the list of rewards {E1:[R11,R12,R13], E2:[R1,R2]}
        TreeMap<Integer,PriorityQueue<Integer>> erm = new TreeMap<Integer,PriorityQueue<Integer>>();
        // AVL Tree somehow doesn't work here. Possibly due to the implementation of predecessor VS floor/lowerEntry/Key
        // Might also be due to constant factor

        int n = sc.nextInt();
        while (n-- > 0) {
            String c = sc.readWord();
            int e = sc.nextInt();
            if (c.compareTo("add") == 0) {
                int r = sc.nextInt();
                if (erm.get(e) == null) {
                    // Construct a binary max heap, add the first reward
                    PriorityQueue<Integer> pq = new PriorityQueue<Integer>(Comparator.reverseOrder());
                    pq.add(r);
                    // Put the PQ to the TreeMap
                    erm.put(e,pq);
                } else { // The PQ with energy e exists, just add to the PQ
                    erm.get(e).add(r);
                }
            } else { // the command is query
                long ans = 0;
                Integer curr = erm.floorKey(e); // cannot use int since we are checking if it's not null
                while (curr != null) {
                    ans += erm.get(curr).poll(); // complete a quest
                    e -= curr; // decrement energy

                    if (erm.get(curr).size() == 0) { // delete the key if PQ is empty
                                                     // use to be for optimization, but considering the case 5-4-1, just remove
                        erm.remove(curr);
                    }

                    // Check case where we decrement 7 from 5-4-1, we skip 4, so floorKey not only if PQ is empty
                    curr = erm.floorKey(e); // move to the lower/same energy
                }
                
                writer.println(ans);
            }
        }
        writer.flush();
    }
}