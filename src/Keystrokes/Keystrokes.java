import java.io.*;
import java.util.*;

public class Keystrokes {
    public static void main(String[] args) throws IOException {
        InputStreamReader inp = new InputStreamReader(System.in);
        BufferedReader sc = new BufferedReader(inp);
        PrintWriter writer = new PrintWriter(System.out);
        
        LinkedList ll = new LinkedList();
        Node curr = ll.head;
        String line = sc.readLine();

        for (int i = 0; i < line.length(); i++) {
            if (line.charAt(i) == 'L') {
                if (curr.prev != null) {
                    curr = curr.prev;
                }
            } else if (line.charAt(i) == 'R') {
                if (curr.next != null) {
                    curr = curr.next;
                }
            } else if (line.charAt(i) == 'B') {
                if (curr.prev != null) {
                    Node temp = curr.prev;
                    ll.delete(curr);
                    curr = temp;
                }
            } else {
                ll.insert(curr, new Node(line.charAt(i)));
                curr = curr.next;
            }
        }

        Node p = ll.head.next;
        while (p != null) {
            writer.print(p.val);
            p = p.next;
        }
        writer.flush();
    }
}

class LinkedList {
    public Node head;
    
    public LinkedList () {
        this.head = new Node(' ');
    }

    public void insert (Node curr, Node newNode) { // O(1)
        newNode.next = curr.next;
        curr.next = newNode;
        newNode.prev = curr;
        if (newNode.next != null)
            newNode.next.prev = newNode;
    }

    public void delete (Node curr) { // O(1)
        if (curr.prev != null) {
            if (curr.next != null) {
                curr.prev.next = curr.next;
                curr.next.prev = curr.prev;
            } else {
                curr.prev.next = null;
            }
        } else {
            if (curr.next != null) {
                curr.next.prev = null;
            }
            // no handling for empty LL
        }
    }
}

class Node {
    public char val;
    public Node next;
    public Node prev;

    public Node (Character s) {
        this.val = s;
        this.next = null;
        this.prev = null;
    }
}