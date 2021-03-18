import java.io.*;
import java.util.*;

public class KattissQuest {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        // This is a map of energy and the list of rewards {E1:[R11,R12,R13], E2:[R1,R2]}
        TreeMap<Integer,PriorityQueue<Integer>> erm = new TreeMap<Integer,PriorityQueue<Integer>>();
        // AVL Tree somehow doesn't work here. Possibly due to the implementation of predecessor VS floor/lowerEntry/Key
        // Might also be due to constant factor

        int n = Integer.parseInt(sc.readLine());
        while (n-- > 0) {
            String[] line = sc.readLine().split(" ");
            String c = line[0];
            int e = Integer.parseInt(line[1]);
            if (c.compareTo("add") == 0) {
                int r = Integer.parseInt(line[2]);
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