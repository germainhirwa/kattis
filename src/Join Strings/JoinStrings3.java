// Final version, passes all test cases

import java.io.*;
import java.util.*;

public class JoinStrings3 {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);

        List<String> strings = new ArrayList<String>(); // list of the strings

        // Create a hashmap to store the indexes and the links between them and for easier access (O(1))
        Map<Integer,IndexNode> hm = new HashMap<Integer,IndexNode>();

        int queries = Integer.parseInt(sc.readLine());

        // The flag boolean and lastIndex integer keep track the position of the last string standing
        int flag = queries;
        int lastIndex = 0;
        
        // Set all the nodes into the hashmap then we will link them after this
        for (int i = 0; i < queries; i++) {
            strings.add(sc.readLine());
            hm.put(i+1,new IndexNode(i+1));
        }

        if (queries > 1) {
            for (int j = 0; j < queries-1; j++, flag--) {
                String[] nums = sc.readLine().split(" ");
                int n1 = Integer.parseInt(nums[0]);
                int n2 = Integer.parseInt(nums[1]);

                // Links the Node n1 with Node n2 by connecting the tail of n1 LL with head of n2, then adjust their last element to be the same
                hm.get(n1).setNext(hm.get(n2));
                
                if (flag == 2) {
                    lastIndex = n1;
                }
            }
            
            // Simply print the strings in order of the indexes based on the linked list
            IndexNode cur = hm.get(lastIndex);
            for (int k = 0; k < queries; k++) {
                writer.print(strings.get(cur.getItem()-1));
                cur = cur.next;
            }
        } else { // edge case one string only, just print itself
            writer.print(strings.get(0));
        }

        writer.flush();
    }
}

// Index Node object is basically similar to a linked list but it contains next and last instead of just next (and prev)
class IndexNode {
    public int item;
    public IndexNode next;
    public IndexNode last;

    // Default constructor
    public IndexNode(int val) { this(val, null); }

    public IndexNode(int val, IndexNode n) { 
        item = val; 
        next = n;
        last = this;
    }

    public IndexNode getNext() { return next; }
    public int getItem() { return item; }

    // We need to keep track of the last node in the linked list
    public void setNext(IndexNode n) {
        last.next = n;
        last = n.last;
    }
}