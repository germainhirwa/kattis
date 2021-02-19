// Optimized but RTE

import java.io.*;
import java.util.*;

public class JoinStrings2 {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        List<String> strings = new ArrayList<String>(); // list of the strings
        Map<Integer,TailedLinkedList> hm = new HashMap<Integer,TailedLinkedList>();

        int queries = Integer.parseInt(sc.readLine());
        int flag = queries;
        int lastIndex = 0;
        
        for (int i = 0; i < queries; i++) {
            strings.add(sc.readLine());
        }

        if (queries > 1) {
            for (int j = 0; j < queries-1; j++, flag--) {
                String[] nums = sc.readLine().split(" ");
                int n1 = Integer.parseInt(nums[0]);
                int n2 = Integer.parseInt(nums[1]);

                if (hm.containsKey(n1)) {
                    if (hm.containsKey(n2)) {
                        hm.get(n1).tail.setNext(hm.get(n2).head);
                        hm.get(n1).tail = hm.get(n2).head;
                    } else {
                        hm.get(n1).addBack(n2);
                    }
                } else {
                    TailedLinkedList concat = new TailedLinkedList();
                    concat.addBack(n1);
                    if (hm.containsKey(n2)) {
                        concat.tail.setNext(hm.get(n2).head);
                        concat.tail = hm.get(n2).tail;
                    } else {
                        concat.addBack(n2);
                    }
                    hm.put(n1,concat);
                }
                
                if (flag == 2) {
                    lastIndex = n1;
                }
            }
            
            TailedLinkedList finalLL = hm.get(lastIndex);
            ListNode cur = finalLL.head;
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

class ListNode {
    public int item;
    public ListNode next;

    public ListNode(int val) { this(val, null); }

    public ListNode(int val, ListNode n) { 
        item = val; 
        next = n; 
    }

    public ListNode getNext() { return next; }
    public int getItem() { return item; }
    public void setItem(int val) { item = val; }
    public void setNext(ListNode n) { next = n; }
}

class TailedLinkedList {
    public ListNode head;
    public ListNode tail;

    public int getFirst() { return head.getItem(); }
    public int getLast() { return tail.getItem(); }

    public void addFront(int item) {
        ListNode newNode = new ListNode(item);
        insert(null,newNode); 
    }
    public void addBack(int item) {
        ListNode newNode = new ListNode(item);
        insert(tail,newNode); 
    }
    public void insert(ListNode cur, ListNode n) {
        if (cur == null) {
            n.setNext(head);
            head = n;
            if (tail == null)
                tail = head;
        }
        else {
            n.setNext(cur.getNext());
            cur.setNext(n);
            if (cur == tail)
                tail = tail.getNext();
        }
    }
}