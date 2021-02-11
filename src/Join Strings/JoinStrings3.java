// Final version, passes all test cases

import java.io.*;
import java.util.*;

public class JoinStrings3 {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        List<String> strings = new ArrayList<String>(); // list of the strings
        Map<Integer,IndexNode> hm = new HashMap<Integer,IndexNode>();

        int queries = Integer.parseInt(sc.readLine());
        int flag = queries;
        int lastIndex = 0;
        
        for (int i = 0; i < queries; i++) {
            strings.add(sc.readLine());
            hm.put(i+1,new IndexNode(i+1));
        }

        if (queries > 1) {
            for (int j = 0; j < queries-1; j++, flag--) {
                String[] nums = sc.readLine().split(" ");
                int n1 = Integer.parseInt(nums[0]);
                int n2 = Integer.parseInt(nums[1]);

                hm.get(n1).setNext(hm.get(n2));
                
                if (flag == 2) {
                    lastIndex = n1;
                }
            }
            
            IndexNode cur = hm.get(lastIndex);
            for (int k = 0; k < queries; k++) {
                writer.print(strings.get(cur.getItem()-1));
                cur = cur.next;
            }
        } else {
            writer.print(strings.get(0));
        }

        writer.flush();
    }
}

class IndexNode {
    public int item;
    public IndexNode next;
    public IndexNode last;

    public IndexNode(int val) { this(val, null); }

    public IndexNode(int val, IndexNode n) { 
        item = val; 
        next = n;
        last = this;
    }

    public IndexNode getNext() { return next; }
    public int getItem() { return item; }
    public void setNext(IndexNode n) {
        last.next = n;
        last = n.last;
    }
}